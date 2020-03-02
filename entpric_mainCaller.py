import json, boto3, logging
from botocore.vendored import requests

client = boto3.client("lambda")
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def convertToList(string):
    li = list(string.split(","))
    mdWeeks = []
    for i in li:
        mdWeeks.append(int(i))

    return mdWeeks



def callLambda(func_name, inp):
    response = client.invoke(
        FunctionName=func_name,
        InvocationType='RequestResponse',
        Payload=json.dumps(inp))
    return json.loads(response["Payload"].read())


def putFirehoseMsg(func_name, del_stream_name, container):
    print("Inside putFirehoseMsg.....")
    client = boto3.client('firehose')
    response = client.put_record(
        DeliveryStreamName=del_stream_name,
        Record={
            'Data': json.dumps(container) + ","
        })
    print("response:::::", response)


def putSQSMessage(func_name, container):
    print("putting message to sqs out queue::::::", func_name)
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='entpric-clxprc-sears-model-output')
    response = queue.send_message(MessageBody=json.dumps(container))


def failCheck(in_cont, fn_name, container):
    print("Inside failCheck::::", fn_name)
    try:
        if (in_cont['message'] != None):
            print("1:::::::")
            container['message'] = in_cont['message']
        if (in_cont['status'] == "Fail"):
            print("3:::::::")
            container['status'] = "Fail"
            if (container['eventSrc'] == "aws:sqs"):
                print("2:::::::")
                putFirehoseMsg(fn_name, 'entpric_clx_sears_del_stream_dropped', container)
                # putSQSMessage(fn_name,container)
                return False
            else:
                return True
    except:
        print("error:::::::")
        container['status'] = "Fail"
        container['message'] = "Unexpected error in " + fn_name + " service: " + str(in_cont)
        return True
    return False


def lambda_handler(event, context):
    # TODO implement
    print("Inside Lambda_handler of mainCaller.........")
    print("event:::::::::::", event)

    eventLength = 1

    try:
        # print("eventSource:::::::",event['Records'])
        eventSrc = event['Records'][0]['eventSource']
        eventLength = int(len(event['Records']))
    except:
        print("eventSource:::::::Not Known")
        eventSrc = None

    print("Records Length:::::::::::", eventLength)

    container = {}
    for x in range(eventLength):
        if (eventSrc == "aws:sqs"):
            body = event['Records'][x]['body']
            input_json = json.loads(str(body))
            # print("decoded_json::::::::::",input_json)
            div_no = int(input_json["div_no"])
            item_no = int(input_json["itm_no"])
            store_no = int(input_json["loc_no"])
            end_date = input_json["end_date"]
            num_weeks_sales = input_json["num_week_sales"]

            mdWeeks = convertToList(input_json["markdown_weeks"])
            onlyWinner = input_json["onlywinner"]
            ssn_name = input_json["ssn_name"]
            eff_date = input_json["effective_date"]
            plan_name = input_json["plan_name"]
            mdl_name = input_json["mdl_name"]
            bu = input_json["bu"]
        else:
            div_no = int(event["div_no"])
            item_no = int(event["item_no"])
            store_no = int(event["store_no"])
            end_date = event["end_date"]
            num_weeks_sales = event["num_weeks_sales"]

            mdWeeks = convertToList(event["markdown_weeks"])
            onlyWinner = event["onlyWinner"]
            ssn_name = event["ssn_name"]
            eff_date = event["effective_date"]
            plan_name = event["plan_name"]
            mdl_name = event["mdl_name"]
            bu = event["bu"]

        print("div_no:::::::::", div_no)
        print("item_no:::::::::", item_no)
        print("store_no:::::::::", store_no)
        print("end_date:::::::::", end_date)
        print("num_weeks_sales:::::::::", num_weeks_sales)
        print("mdWeeks:::::::::", mdWeeks)
        print("season name::::::", ssn_name)
        print("eff_date::::::", eff_date)
        print("plan_name::::::", plan_name)
        print("mdl_name::::::", mdl_name)
        print("bu::::::", bu)

        # Setting values in response JSON

        container['div_no'] = div_no
        container['item_no'] = item_no
        container['store_no'] = store_no
        container['status'] = "Success"
        container['message'] = None
        container['optimization'] = None
        container['eventSrc'] = eventSrc
        container['eff_date'] = eff_date
        container['plan_name'] = plan_name
        container['mdl_name'] = mdl_name
        container['bu'] = bu

        # Calling sku service to get the sku's under given item
        logger.info("*************************Sku Service Start*************************")
        skuList = callLambda('entpric_getSKUList', {'div_no': div_no, 'item_no': item_no})
        print("skuList::::::::::::", skuList)
        print("Length of skuList::::::::::", len(skuList["skuList"]))
        logger.info("*************************Sku Service End*************************")

        if (skuList['status'] == "Success"):
            logger.info("*************************On-hand Inventory Service Start*************************")
            onHandInv = callLambda('entpric_getOnHandInv', {'div_no': div_no, 'item_no': item_no, 'store_no': store_no,
                                                            "skuList": skuList["skuList"]})
            print("onHandInv::::::::", onHandInv)
            logger.info("*************************On-hand Inventory Service End*************************")
            container['on_hand_inv'] = onHandInv["on_hand_inv"]

            print("onHandInv Value is::::", onHandInv["on_hand_inv"])
            if (int(onHandInv["on_hand_inv"]) > 0):
                logger.info("*************************Assumption Merge Service Start*************************")
                mergedSchema = callLambda('entpric_mergeAssumptions',
                                          {'div_no': div_no, 'item_no': item_no, 'store_no': store_no,
                                           "sku_list": skuList["skuList"], "end_date": end_date, "md_weeks": mdWeeks,
                                           "num_weeks_sales": num_weeks_sales, "on_hand_inv": onHandInv["on_hand_inv"],
                                           "ssn_name": ssn_name, "onlyWinner": onlyWinner})
                print("mergedSchema::::::::::::::::::::::::::::", mergedSchema)

                if (failCheck(mergedSchema, "assumption merge", container)):
                    return container
                logger.info("*************************Assumption Merge Service End*************************")

                if (mergedSchema['status'] == "Success"):
                    # container['bu'] = mergedSchema['bu']
                    container['vbs_no'] = mergedSchema['vbs_no']
                    container['line_no'] = mergedSchema['line']
                    container['subline'] = mergedSchema['sbl_no']
                    container['class_no'] = mergedSchema['class_no']
                    container['divDs'] = mergedSchema['divDs']
                    container['Item_Description'] = mergedSchema['Item_Description']
                    container['lnDs'] = mergedSchema['lnDs']
                    container['sublnDs'] = mergedSchema['sublnDs']
                    container['classDs'] = mergedSchema['classDs']
                    container['prdDs'] = mergedSchema['prdDs']
                    container['season_cd'] = mergedSchema['season_cd']
                    container['season_nm'] = mergedSchema['season_nm']
                    container['predicted_units'] = mergedSchema['predicted_sale']
                    container['reg_price'] = mergedSchema['reg_price']
                    container['Current_Disc'] = mergedSchema['disc']
                    # container['fisc_wk_nbr'] = mergedSchema['fisc_wk_nbr']

                    container['sal_value'] = mergedSchema['sal_value']
                    container['on_hand_act'] = mergedSchema['on_hand_act']
                    container['on_hand_top_wk'] = mergedSchema['on_hand_qty']

                    if ssn_name == 'Basics':
                        container['avgWeeklyUnits'] = mergedSchema['avgWeeklyUnits']
                        container['std_dollars'] = mergedSchema['std_dollars']
                        container['units_lwk'] = mergedSchema['units_lwk']
                        container['dollar_lwk'] = mergedSchema['dollar_lwk']
                        container['units_three_wk'] = mergedSchema['units_three_wk']
                        container['dollar_three_wk'] = mergedSchema['dollar_three_wk']
                        container['units_sold'] = mergedSchema['units_sold']
                        container['cost_per_unit'] = mergedSchema['cost_per_unit']

                    container['count'] = eventLength

                    logger.info("*************************Optimization Service Start*************************")
                    optOutput = callLambda('entpric_Optimization', mergedSchema)
                    print("optOutput is:::::", optOutput)
                    logger.info("*************************Optimization Service End*************************")

                    # Invoke IMA service to get plng_id, plng_desc, valu_id, valu_nm for attr_id=420, default is None
                    container["valu_id"] = None
                    container["valu_nm"] = None
                    container['plng_id'] = 0
                    container['plng_desc'] = ""

                    logger.info("*************************IMA Service Start*************************")
                    ima_url = "http://trprkmkdwnapp3.intra.searshc.com:8098/markdown/fetchPlnAttrData"
                    datajson = requests.post(ima_url, json=[{"div_no": div_no, "itm_no": item_no}]).json()
                    print("IMA service response::::: datajson ::::::", datajson)
                    logger.info("*************************IMA Service End*************************")

                    try:
                        attr_id = datajson[0]['attr_id']
                        print("attr_id:::::", attr_id)
                        container['plng_id'] = datajson[0]['planning_id']
                        container['plng_desc'] = datajson[0]['planning_nm']

                        if (attr_id == 420):
                            container["valu_id"] = datajson[0]['valu_id']
                            container["valu_nm"] = datajson[0]['valu_nm']
                    except:
                        print("No valid response from IMA service.")

                    container['optimization'] = optOutput
                    # container['Current_Disc'] = optOutput[currentDiscount]

                    if (eventSrc == "aws:sqs"):
                        # putSQSMessage("entpric_Optimization",container)
                        putFirehoseMsg("entpric_Optimization", 'entpric_clx_sears_del_stream', container)
                    else:
                        return container
            else:

                container['status'] = "Fail"
                container['message'] = 'No optimization needed as inventory is not available.'

                if (eventSrc == "aws:sqs"):
                    putFirehoseMsg("entpric_getOnHandInv", 'entpric_clx_sears_del_stream_dropped', container)
                    # putSQSMessage("entpric_getOnHandInv",container)
                else:
                    return container
        else:

            container['status'] = "Fail"
            container['message'] = "No sku found for given item "
            if (eventSrc == "aws:sqs"):
                putFirehoseMsg("entpric_getSKUList", 'entpric_clx_sears_del_stream_dropped', container)
                # putSQSMessage("entpric_getSKUList",container)
            else:
                return container
            return container
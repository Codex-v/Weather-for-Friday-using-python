def get_single_product_details(product_link):
    driver.delete_cookie("ak_bmsc")
    driver.get(product_link)
    sleep(3)
    data = re.search(r"window\['__PRELOADED_STATE__'] = (\{.*?})<", driver.page_source)
    data = json.loads(data.group(1))
    product_id_from_json = data["productId"]
    product_details_from_json = data["productDetails"][product_id_from_json]

    product_data = product_details_from_json["product"]
    location_data = product_details_from_json["location"]
    inventory_data = product_details_from_json["itemInventory"]


    try:
        title = product_data["title"]
    except:
        title = "N/A"
    try:
        brand = product_data["brand"]
    except:
        brand = "N/A"

    try:
        upc = product_data["barcode"]
    except:
        upc = "N/A"

    try:
        item_number = product_data["itemNumber"]
    except:
        item_number = "N/A"

    try:
        model_number = product_data["modelId"]
    except:
        model_number = "N/A"

    try:
        price = location_data["price"]["pricingDataList"][0]["finalPrice"]
    except:
        price = "N/A"

    try:
        free_shipping = location_data["promotion"]["freeDelivery"]
    except:
        free_shipping = "N/A"

    try:
        available_for_delivery = inventory_data["analyticsData"]["parcel"]["availabilityStatus"]
    except:
        available_for_delivery = "N/A"

    try:
        available_quantity_for_delivery = inventory_data["analyticsData"]["parcel"]["availableQuantity"]
    except:
        available_quantity_for_delivery = "N/A"

    cost_of_delivery = "N/A"


    # if not free_shipping:
    sleep(1)
    cost = driver.execute_script(
        """return document.evaluate('(//div[contains(@class, "fulfilment-messages")])[2]/div[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue?.innerText""")

    delivery_date = "N/A"
    if cost is not None:
        parts = cost.split(':')
        delivery_date = parts[0]
        if len(parts) == 2:
            cost_of_delivery = parts[1].replace('From', '').strip()


    product_details = {
        "product url":product_link,
        "brand": brand,
        "title": title,
        "upc": upc,
        "itemNumber": item_number,
        "modelNumber": model_number,
        "price": price,
        "availableForDelivery": available_for_delivery,
        "availableQuantityForDelivery": available_quantity_for_delivery,
        "freeShipping": free_shipping,
        "costOfDelivery": cost_of_delivery,
        "deliveryDate":delivery_date
    }

    return product_details

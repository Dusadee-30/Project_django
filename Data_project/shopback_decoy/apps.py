from django.apps import AppConfig


class ShopbackDecoyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopback_decoy'

URL_WEB_SHOPEE      = 'https://shopee.th'
HEADER_SHOPEE       = {
    "User-Agent":   "Chrome",
    "Referer":      "{shopee}search?keyword={keyword}"
}
URL_SEARCH_SHOPEE   = "https://shopee.co.th/api/v4/search/search_items?by=relevancy&keyword={keyword}&limit=10&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2"
URL_IMAGE_SHOPEE = "https://cf.shopee.co.th/file/"
URL_LINK_ITEM_SHOPEE = "https://shopee.co.th/"
URL_RATING_SHOPEE = "https://shopee.sg/api/v2/item/get_ratings?filter=0&flag=1&itemid={item}&limit=20&offset={off_set}&shopid={shop}&type=0"

URL_WEB_JD_CENTRAL      = 'https://www.jd.co.th/'
HEADER_JD_CENTRAL       = {
    "User-Agent":   "Chrome",
    "Referer":      "{jd_central}search/{keyword}.html"
}
URL_SEARCH_JD_CENTRAL   = "https://api.jd.co.th/client.action?body=%7B%22page%22%3A%221%22%2C%22pagesize%22%3A%2210%22%2C%22cid%22%3A%22%22%2C%22filed%22%3A%22%22%2C%22expandName%22%3A%7B%7D%2C%22brand%22%3A%22%22%2C%22isCorrect%22%3A%221%22%2C%22sort%22%3A%220%22%2C%22stock%22%3A1%2C%22keyword%22%3A%22{keyword}%22%7D&functionId=search&client=pc&clientVersion=2.0.0&lang=th_TH&area=&"
URL_LINK_ITEM_JD_CENTRAL = "https://www.jd.co.th/product/{wname}_{wareId}.html"

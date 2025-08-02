import logging
import azure.functions as func
from agent.tools.query_tool import search_trades_by_field

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request for search_trades_by_field.')
    try:
        req_body = req.get_json()
        field = req_body.get('field')
        value = req_body.get('value')
        if not field or not value:
            return func.HttpResponse("Missing 'field' or 'value'.", status_code=400)
        result = search_trades_by_field(field, value)
        return func.HttpResponse(result, mimetype="application/json")
    except Exception as e:
        logging.error(f"Exception: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

from flask.views import MethodView
from app.decorators import validate_request
from app.common_utils import render_success_response
from app.v1.users.service import SubApp1Service


class GetUserName(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response()
        return render_success_response(response, message)

class GetUserProfile(MethodView):
    @validate_request
    def get(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response1()
        return render_success_response(response, message)

class GetUserQuotes(MethodView):
    @validate_request
    def post(self, params, headers, *args, **kwargs):
        response, message = SubApp1Service(params, headers).get_static_api_response2()
        return render_success_response(response, message)       
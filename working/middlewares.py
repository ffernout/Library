from django.utils.deprecation import MiddlewareMixin
from .models import CustomUser

class SalaryAndPositionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            try:
                user = request.user
                if user.degree:
                    position, salary = self.get_position_and_salary(user.degree)
                    user.position = position
                    user.salary = salary
                    user.save()
            except CustomUser.DoesNotExist:
                pass
        return None


    def get_position_and_salary(self, degree):
        if degree == "Бакалавр":
            return "Младший библиотекарь", 1500.00
        elif degree == "Магистр":
            return "Библиотекарь", 2500.00
        elif degree == "Аспирант":
            return "Старший библиотекарь", 3500.00
        return "Младший библиотекарь", 1500.00
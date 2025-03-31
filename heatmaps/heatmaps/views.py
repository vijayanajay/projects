from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render


def home(request):
    """View for the home page."""
    return render(request, "home.html")


def test_db(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            row = cursor.fetchone()
            return JsonResponse(
                {
                    "status": "success",
                    "message": "Database connection successful",
                    "result": row[0],
                }
            )
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

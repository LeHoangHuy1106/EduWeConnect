import os

import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from advise.serializer import DataScoreSerializer


# Đường dẫn đến tệp CSV từ root của dự án Django
csv_file_path = os.path.join(settings.BASE_DIR, 'Data', 'data_with_space_delimiter.csv')

# Đọc DataFrame từ tệp CSV
df = pd.read_csv(csv_file_path,encoding='utf-8')

class DataScore(APIView):
    def get(self, request, code, *args, **kwargs):
        global df
        # Lọc các hàng có mã trường tương ứng
        code= "".join([code,' '])
        filtered_data = df[df['ID'] == code]
        # Chuyển kết quả thành danh sách từ điển
        result_data = filtered_data.to_dict(orient='records')
        # Serialize danh sách từ điển thành JSON
        serializer = DataScoreSerializer(result_data, many=True)
        return Response(serializer.data)
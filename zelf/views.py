import json
import httpx
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from zelf.serializers import ContentListSerializer
from zelf.services import get_content_url, get_headers
import logging
import requests

logger = logging.getLogger(__name__)


class ContentListView(ViewSet):
    def list(self, request, *args, **kwargs):
        try:
            page = self.request.GET.get("page")
            content_url = get_content_url(page)

            with httpx.Client() as client:
                content_response = client.get(content_url, headers=get_headers())
                content_response.raise_for_status()
                content_data = json.loads(content_response.text)
                logger.info(f"Response Successful from content Data")

            serializer = ContentListSerializer(data=content_data.get('data'), many=True)
            serializer.is_valid(raise_exception=True)
            logger.info(f"Response Successful")
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except httpx.RequestError as e:
            return Response(data={"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AggregatedStatsView(ViewSet):
    def list(self, request, *args, **kwargs):
        url = 'http://127.0.0.1:8000/api/zelf/content-list/?page=1'
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        raw_data = json.loads(response.text)[0]

        total_likes = sum(entry['stats']['digg_counts']['likes']['count'] for entry in raw_data)
        total_views = sum(entry['stats']['digg_counts']['views']['count'] for entry in raw_data)
        total_comments = sum(entry['stats']['digg_counts']['comments']['count'] for entry in raw_data)

        num_entries = len(raw_data)
        average_likes = total_likes / num_entries
        average_views = total_views / num_entries
        average_comments = total_comments / num_entries

        aggregated_stats = {
            "total_likes": total_likes,
            "total_views": total_views,
            "total_comments": total_comments,
            "average_likes": average_likes,
            "average_views": average_views,
            "average_comments": average_comments,
        }
        return Response(aggregated_stats)

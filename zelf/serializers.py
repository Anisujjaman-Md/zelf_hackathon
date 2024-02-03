import requests
from rest_framework import status
from rest_framework.response import Response
import logging
import json
from rest_framework import serializers
from zelf.services import get_author_url, get_headers

logger = logging.getLogger(__name__)


class ContentListSerializer(serializers.Serializer):
    def to_representation(self, data):
        # Check if 'author' key exists in the initial data
        author_dic = {}
        for _data in self.initial_data:
            if 'author' in _data:
                author_data = _data['author']
                if isinstance(author_data, dict):
                    author_id = author_data.get("id")
                    author_url = get_author_url(author_id) if author_id else None
                    if author_id in author_dic:
                        _data["author"] = author_dic[author_id]
                    else:
                        # Fetch author data
                        if author_url:
                            try:
                                author_response = requests.get(author_url, headers=get_headers())
                                author_response.raise_for_status()
                                author_data = json.loads(author_response.text).get("data")
                                author_dic[author_id] = author_data
                                # Update the initial_data with the new author data
                                _data["author"] = author_data
                            except requests.RequestException as e:
                                logger.error(f"Error in AuthorView: {str(e)}")
                                pass

        # Return the modified initial_data
        return self.initial_data


class DataEntrySerializer(serializers.Serializer):
    unique_id = serializers.IntegerField()
    author = serializers.ListField()
    stats = serializers.DictField()

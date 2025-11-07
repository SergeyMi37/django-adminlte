# views.py
from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample
from appmsw.models import Param, Comment
from appmsw.serializers import ParamSerializer, CommentSerializer

@extend_schema_view(
    list=extend_schema(
        description='Получить список всех параметров',
        summary='Список параметров',
        parameters=[
            OpenApiParameter(
                name='category',
                description='Фильтр по категории',
                required=False,
                type=str
            ),
            OpenApiParameter(
                name='public',
                description='Фильтр по публичности',
                required=False,
                type=bool
            )
        ]
    ),
    retrieve=extend_schema(
        description='Получить детальную информацию о параметре',
        summary='Детали параметра'
    ),
    create=extend_schema(
        description='Создать новый параметр',
        summary='Создание параметра',
        examples=[
            OpenApiExample(
                'Пример создания параметра',
                value={
                    'name': 'Название параметра',
                    'category': 'app',
                    'desc': 'Описание параметра',
                    'option': 'Опции',
                    'json': '{"key": "value"}',
                    'public': True
                }
            )
        ]
    ),
    update=extend_schema(
        description='Обновить параметр полностью',
        summary='Полное обновление параметра'
    ),
    partial_update=extend_schema(
        description='Частично обновить параметр',
        summary='Частичное обновление параметра'
    ),
    destroy=extend_schema(
        description='Удалить параметр',
        summary='Удаление параметра'
    )
)
class ParamViewSet(viewsets.ModelViewSet):
    queryset = Param.objects.all()
    serializer_class = ParamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        queryset = Param.objects.all()
        category = self.request.query_params.get('category')
        public = self.request.query_params.get('public')
        
        if category:
            queryset = queryset.filter(category=category)
        if public:
            queryset = queryset.filter(public=public.lower() == 'true')
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@extend_schema_view(
    list=extend_schema(
        description='Получить список комментариев',
        summary='Список комментариев'
    ),
    retrieve=extend_schema(
        description='Получить детальную информацию о комментарии',
        summary='Детали комментария'
    ),
    create=extend_schema(
        description='Создать новый комментарий',
        summary='Создание комментария',
        examples=[
            OpenApiExample(
                'Пример создания комментария',
                value={
                    'text': 'Текст комментария',
                    'param': 1
                }
            )
        ]
    ),
    update=extend_schema(
        description='Обновить комментарий полностью',
        summary='Полное обновление комментария'
    ),
    partial_update=extend_schema(
        description='Частично обновить комментарий',
        summary='Частичное обновление комментария'
    ),
    destroy=extend_schema(
        description='Удалить комментарий',
        summary='Удаление комментария'
    )
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
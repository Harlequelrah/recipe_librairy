from app.recipe.models import Entity  # remplacer par l'entité SQLAlchemy
from app.recipe.schemas import (  # remplacer par les modèles Pydantic
    EntityCreateModel,
    EntityFullReadModel,
    EntityPatchModel,
    EntityReadModel,
    EntityUpdateModel,
)
from app.settings.config.database_config import session_manager
from elrahapi.crud.crud_forgery import CrudForgery
from elrahapi.crud.crud_models import CrudModels

recipe_crud_models = CrudModels(
    entity_name="recipe",
    primary_key_name="id",  # remplacer au besoin par le nom de la clé primaire
    SQLAlchemyModel=Entity,  # remplacer par l'entité SQLAlchemy
    ReadModel=EntityReadModel,
    CreateModel=EntityCreateModel,  # Optionel
    UpdateModel=EntityUpdateModel,  # Optionel
    PatchModel=EntityPatchModel,  # Optionel
    FullReadModel=EntityFullReadModel,  # Optionel
)
recipe_crud = CrudForgery(crud_models=recipe_crud_models, session_manager=session_manager)

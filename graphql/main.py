import strawberry
import uvicorn
from fastapi import FastAPI
from src.config import db
from Graphql.query import Query
from Graphql.mutation import Mutation
from strawberry.fastapi import GraphQLRouter

def init_app():
    async def lifespan(app: FastAPI):
        await db.create_all()
        yield
        await db.close()

    apps = FastAPI(
        title="Learning FastAPI with Strawberry GraphQL",
        description="Fast API",
        version="1.0.0",
        lifespan=lifespan
    )

    @apps.get("/")
    def home():
        return "Welcome home!"
    
    # add graphql endpoint 
    schema = strawberry.Schema(query=Query,mutation=Mutation)
    graphql_app = GraphQLRouter(schema)

    apps.include_router(graphql_app, prefix="/graphql")
    
    return apps 

app = init_app()

if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=8888, reload=True)
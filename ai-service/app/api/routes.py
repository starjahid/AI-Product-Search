from fastapi import APIRouter
from app.models.schemas import ProductRequest
from app.services.analyzer import analyze_product
from app.services.memory import get_cached_product, set_cached_product

router = APIRouter()


@router.get("/")
def root():
    return {"message": "AI Product Search API Running 🚀"}


@router.post("/analyze")
def analyze_product_route(data: ProductRequest):

    try:
        # 🔑 Create cache key
        cache_key = data.name.lower().strip()

        # 📦 Check cache first
        cached = get_cached_product(cache_key)
        if cached:
            return {
                "status": "success",
                "source": "cache",
                "data": cached
            }

        # 🤖 Call AI analyzer
        result = analyze_product(
            name=data.name,
            description=data.description,
            reviews=data.reviews
        )

        # 💾 Save to cache
        if result["analysis"].get("recommendation") != "neutral":
            set_cached_product(cache_key, result)

        return {
            "status": "success",
            "source": "ai",
            "data": result
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
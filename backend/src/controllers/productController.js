import { searchGoogleProducts } from "../services/googleService.js";
import { analyzeProductAI } from "../services/aiService.js";
import { calculateFinalScore } from "../services/scorerService.js";
import { getFacebookPageData } from "../services/facebookService.js";

export const searchProduct = async (req, res) => {
  try {
    const { query } = req.body;

    // 1. Search products from Google
    const products = await searchGoogleProducts(query);

    let finalResults = [];

    for (const product of products) {

      // 2. Send to AI service
      const aiResult = await analyzeProductAI(product);

      // 3. Calculate final score
      const finalScore = calculateFinalScore(aiResult.analysis);

      const fbData = await getFacebookPageData(product.name);

      finalResults.push({
        ...product,
        ...aiResult.analysis,
        facebook: fbData,
        final_score: finalScore
      });
    }

    // 4. Sort best products
    finalResults.sort((a, b) => b.final_score - a.final_score);

    res.json({
      status: "success",
      products: finalResults
    });

  } catch (error) {
    res.status(500).json({
      status: "error",
      message: error.message
    });
  }
};
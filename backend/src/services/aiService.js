import axios from "axios";
import { config } from "../config/env.js";

export const analyzeProductAI = async (product) => {
  try {
    const res = await axios.post(config.AI_SERVICE_URL, {
      name: product.name,
      description: product.description,
      reviews: product.reviews
    });

    return res.data.data;

  } catch (error) {
    return {
      analysis: {
        sentiment_score: 0.5,
        fraud_risk: 0.5,
        trust_score: 50,
        recommendation: "neutral"
      }
    };
  }
};
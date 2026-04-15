import dotenv from "dotenv";
dotenv.config();

export const config = {
  PORT: process.env.PORT || 5000,
  GOOGLE_API_KEY: process.env.GOOGLE_API_KEY,
  GOOGLE_CX: process.env.GOOGLE_CX,
  AI_SERVICE_URL: process.env.AI_SERVICE_URL
};
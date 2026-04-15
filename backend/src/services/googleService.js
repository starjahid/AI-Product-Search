import axios from "axios";
import { config } from "../config/env.js";

export const searchGoogleProducts = async (query) => {
  try {
    const url = `https://www.googleapis.com/customsearch/v1?q=${query}&key=${config.GOOGLE_API_KEY}&cx=${config.GOOGLE_CX}`;

    const res = await axios.get(url);

    return res.data.items.map(item => ({
      name: item.title,
      description: item.snippet,
      link: item.link,
      reviews: [] // will improve later
    }));

  } catch (err) {
    console.error("Google API error:", err.message);
    return [];
  }
};
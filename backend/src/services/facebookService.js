import axios from "axios";

const FB_API = "https://graph.facebook.com/v18.0";

/**
 * Get basic Facebook page info (rating, followers)
 */
export const getFacebookPageData = async (pageName) => {
  try {
    const url = `${FB_API}/${pageName}?fields=name,fan_count,overall_star_rating&access_token=${process.env.FB_ACCESS_TOKEN}`;

    const res = await axios.get(url);

    return {
      name: res.data.name,
      followers: res.data.fan_count || 0,
      rating: res.data.overall_star_rating || 0
    };

  } catch (err) {
    console.error("Facebook API error:", err.message);

    return {
      name: pageName,
      followers: 0,
      rating: 0
    };
  }
};
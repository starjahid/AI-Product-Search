import express from "express";
import { searchProduct } from "../controllers/productController.js";

const router = express.Router();

router.get("/", (req, res) => {
  res.send("API Running");
});

router.post("/search", searchProduct);

export default router;
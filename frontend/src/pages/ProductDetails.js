import axios from "axios";
import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";

export default function ProductDetails() {
  const [product, setProduct] = useState("");

  const { slug } = useParams();

  const getSingleProduct = async () => {
    const { data } = await axios.get(
      `http://localhost:8000/api/products/${slug}/`
    );
    setProduct(data);
  };

  useEffect(() => {
    getSingleProduct();
  }, []);

  return (
    <div className="product--details--main">
      <div className="details--info">
        <h1 className="album--name--details">{product.album}</h1>
        <div>
          <p className="details--desc">Album description:</p>
          <p>{product.description}</p>
        </div>
        <div className="details--num--tape">
          <p>{product.label_number}</p>
          <p>{product.physical_type}</p>
        </div>
        <div className="details--price">
          <p>Price: {product.price}</p>
        </div>
      </div>
      <div className="details--img">
        <img src={product.cover_art_img} className="details--album--img"></img>
      </div>
    </div>
  );
}

import { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

export default function Products() {
  const [products, setProducts] = useState([]);

  const getProducts = async () => {
    const response = await axios.get("http://localhost:8000/api/products/");
    setProducts(response.data);
  };

  useEffect(() => {
    getProducts();
  }, []);

  return (
    <div className="products--main">
      {products.map((product, index) => (
        <Link to={`/${product.slug}`}>
          <div className="product--info">
            <img src={product.cover_art_img} className="product--img"></img>
            <p className="product--artist">{product.artist}</p>
            <p className="album--name">{product.album}</p>
            <p className="album--genre">{product.genre}</p>
            <div className="album--date--country">
              <p>{product.country}</p>
              <p>{product.release_date}</p>
            </div>
          </div>
        </Link>
      ))}
    </div>
  );
}

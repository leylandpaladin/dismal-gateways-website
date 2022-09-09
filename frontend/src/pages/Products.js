import { Link } from "react-router-dom";
import { useGetAllProductsQuery } from "../features/productsApi";

export default function Products() {
  const { data, error, isLoading } = useGetAllProductsQuery("");

  return (
    <div className="products--main">
      {isLoading ? (
        <p>Loading</p>
      ) : error ? (
        <p>An error occured</p>
      ) : (
        <>
          {data.map((product) => (
            <div key={product.slug} className="product--info">
              <Link to={`${product.slug}`}>
                <img src={product.cover_art_img} className="product--img"></img>
                <p className="product--artist">{product.artist}</p>
                <p className="album--name">{product.album}</p>
                <p className="album--genre">{product.genre}</p>
                <div className="album--date--country">
                  <p>{product.country}</p>
                  <p>{product.release_date}</p>
                </div>
              </Link>
            </div>
          ))}
        </>
      )}
    </div>
  );
}

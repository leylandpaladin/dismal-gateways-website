import { useGetSingleProductQuery } from "../features/productsApi";

export default function ProductDetails() {
  const { data, error, isLoading } = useGetSingleProductQuery("");

  return (
    <>
      <div className="product--details--main">
        {isLoading ? (
          <p>Loading</p>
        ) : error ? (
          <p>An error occured</p>
        ) : (
          <>
            {data.map((product) => (
              <>
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
                  <img
                    src={product.cover_art_img}
                    className="details--album--img"
                  ></img>
                </div>
              </>
            ))}
          </>
        )}
      </div>
    </>
  );
}

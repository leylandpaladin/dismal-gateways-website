import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const productsAPI = createApi({
  reducerPath: "productsApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  endpoints: (builder) => ({
    getAllProducts: builder.query({
      query: () => "products/",
    }),
  }),
});

export const productAPI = createApi({
  reducerPath: "productApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  endpoints: (builder) => ({
    getSingleProduct: builder.query({
      query: (slug) => `products/${slug}`,
    }),
  }),
});

export const { useGetAllProductsQuery } = productsAPI;
export const { useGetSingleProductQuery } = productAPI;

import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const productsAPI = createApi({
  reducerPath: "productsApi",
  baseQuery: fetchBaseQuery({ baseUrl: "http://localhost:8000/api/" }),
  endpoints: (builder) => ({
    getAllProducts: builder.query({
      query: () => "products/",
    }),
    getSingleProduct: builder.query({
      query: (slug) => `products/${slug}`,
    }),
  }),
});

export const { useGetAllProductsQuery, useGetSingleProductQuery } = productsAPI;

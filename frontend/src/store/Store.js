import { configureStore } from "@reduxjs/toolkit";
import productsReducer from "../features/productsSlice";
import { productsAPI, productAPI } from "../features/productsApi";
import { setupListeners } from "@reduxjs/toolkit/dist/query";

export const store = configureStore({
  reducer: {
    products: productsReducer,
    [productsAPI.reducerPath]: productsAPI.reducer,
    product: productsReducer,
    [productAPI.reducerPath]: productAPI.reducer,
  },
  middleware: (getDefaultMiddleware) => {
    return (
      getDefaultMiddleware().concat(productsAPI.middleware),
      getDefaultMiddleware().concat(productAPI.middleware)
    );
  },
});

setupListeners(store.dispatch);

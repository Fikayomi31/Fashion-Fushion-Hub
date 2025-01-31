import { create } from "zustand";
import { devtools } from "zustand/middleware";

const useAuthStore = create(
  devtools((set, get) => ({
    allUserData: null,
    loading: false,

    user: () => ({
      user_id: get().allUserData?.user_id || null,
      username: get().allUserData?.username || null,
    }),

    setUser: (user) => set({ allUserData: user }),
    setLoading: (loading) => set({ loading }),

    isLoggedIn: () => get().allUserData !== null,
  }))
);

export { useAuthStore };

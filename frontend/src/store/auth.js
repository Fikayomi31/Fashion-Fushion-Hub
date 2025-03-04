import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { mountStoreDevtool } from 'simple-zustand-devtools';

const useAuthStore = create(
    persist(
        (set, get) => ({
            allUserData: null, 
            loading: false,
            user: () => ({
                user_id: get().allUserData?.user_id || null,
                username: get().allUserData?.username || null,
                vendor_id: get().allUserData?.vendor_id || null,
            }),
            setUser: (user) => set({ allUserData: user }),
            setLoading: (loading) => set({ loading }),
            isLoggedIn: () => get().allUserData !== null,
            logout: () => set({ allUserData: null }),
        }),
        {
            name: 'auth-storage', // key for localStorage
            // Optional: specify which parts of the state to persist
            partialize: (state) => ({
                allUserData: state.allUserData
            })
        }
    )
);

if (import.meta.env.DEV) {
    mountStoreDevtool('Store', useAuthStore);
}

export { useAuthStore };
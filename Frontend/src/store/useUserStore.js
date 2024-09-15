import { create } from 'zustand';

const useUserStore = create((set) => ({
  email: '',
  languagePreference: 'English',

  setEmail: (email) => set(() => ({ email })),
  setLanguagePreference: (languagePreference) => set(() => ({ languagePreference })),
}));

export default useUserStore;
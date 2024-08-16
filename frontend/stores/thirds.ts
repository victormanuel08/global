
import { ref } from 'vue';
import { createGlobalState } from '@vueuse/core';

const initialThirdObject = {};
const initialUser = {};

export const useThirdObject = createGlobalState(() => {
  const thirdObject = ref(initialThirdObject);
  return { thirdObject };
});


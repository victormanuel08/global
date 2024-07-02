export type Pagination = {
  page: number; // Acá se guarda el número de página actual
  pageSize: number; // Acá se guarda la cantidad de resultados por página
  resultsCount: number; // Acá se guarda la cantidad total de resultados
};

export interface PaginatedApiResult<T> {
  count: number;
  next: string;
  previous: string;
  results: T[];
}

export const usePaginatedFetch = <T>(url: string | Ref<string>, filters=ref({}) as Ref | ComputedRef ) => {
  const search = ref("");
  // Este composable ya le resuelve todo el asunto de la paginacion, no necesita que se le pase la pagina
  const pagination = reactive({
    page: 1,
    pageSize: 10,
    resultsCount: 0,
  } as Pagination);  

  const { page, pageSize, resultsCount } = toRefs(pagination);

  //const sanitizedFilters = computed(() => usePickBy(filters.value, (value: any) => Boolean(value)));

  const query = computed(() => {
    return {
      page: page.value,
      page_size: pageSize.value,
      search: search.value,
      //...sanitizedFilters.value
    };
  })


  const {
    data: rawData,
    pending,
    status,
    refresh,
  } = useFetch<PaginatedApiResult<T>>(url, {
    method: "GET",
    query
  });

  watchEffect(() => {
    resultsCount.value = rawData.value?.count || 0;
  });

  watch(search, () => {
    page.value = 1;
  });

  const data = computed(() => rawData.value?.results || []);

  return {
    data,
    pageSize,
    page,
    status,
    resultsCount,
    filters,
    pending,
    search,
    refresh,
    pagination,
    usePaginatedFetch
  };
};


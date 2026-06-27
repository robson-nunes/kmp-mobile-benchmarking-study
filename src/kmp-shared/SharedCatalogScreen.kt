@Composable
fun SharedCatalogScreen(viewModel: SharedViewModel) {
    // Observacao de estados reativos unificados
    val products by viewModel.products.collectAsState()
    val isLoading by viewModel.isLoading.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Catalogo KMP") },
                actions = {
                    IconButton(
                        onClick = { viewModel.sortProductsByPrice() },
                        enabled = !isLoading && products.isNotEmpty()
                    ) {
                        Icon(Icons.Default.Sort, "Ordenar Preço")
                    }
                }
            )
        }
    ) { paddingValues ->
        LazyColumn(contentPadding = paddingValues) {
            items(products, key = { it.id }) { product ->
                ProductCard(product) // Renderizado pelo Skia
            }
        }
    }
}
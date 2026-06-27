@Composable
fun ProductCatalogScreen(viewModel: ProductViewModel) {
    val products by viewModel.products.collectAsState()
    val isLoading by viewModel.isLoading.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Catalogo Android") },
                actions = {
                    IconButton(
                        onClick = { viewModel.sortProductsByPrice() },
                        enabled = !isLoading && products.isNotEmpty()
                    ) {
                        Icon(Icons.Default.Sort, contentDescription = "Ordenar")
                    }
                }
            )
        }
    ) { padding ->
        LazyColumn(contentPadding = padding) {
            items(products, key = { it.id }) { product ->
                ProductCard(product = product)
            }
        }
    }
}
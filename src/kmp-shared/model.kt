@Serializable
data class Product(
    val id: String,
    val title: String,
    val description: String,
    val price: Double,
    val category: String,
    val rating: Double,
    val inStock: Boolean,
    val imageUrl: String
)
import SwiftUI

struct ContentView: View {
    // Liga a interface a logica assincrona
    @StateObject private var viewModel = ProductViewModel()
    
    var body: some View {
        NavigationView {
            Group {
                if viewModel.isLoading && viewModel.products.isEmpty {
                    VStack {
                        ProgressView().scaleEffect(1.5)
                        Text("A carregar catalogo...").padding(.top)
                    }
                } else {
                    // O componente 'List' no SwiftUI e altamente otimizado para reaproveitamento de celulas
                    List(viewModel.products) { product in
                        ProductRowView(product: product)
                    }
                    .listStyle(PlainListStyle()) // Estilo minimalista para reduzir o overhead visual
                }
            }
            .navigationTitle("Catalogo iOS")
            .task {
                if viewModel.products.isEmpty {
                    await viewModel.loadProducts()
                }
            }
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: {
                        Task { await viewModel.sortProductsByPrice() }
                    }) {
                        Image(systemName: "arrow.up.arrow.down.circle.fill")
                            .font(.title3)
                    }
                    .disabled(viewModel.isLoading || viewModel.products.isEmpty)
                }
            }
        }
    }
}
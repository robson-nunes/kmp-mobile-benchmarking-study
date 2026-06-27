# Kotlin Multiplatform Benchmarking Study

Este repositório contém os artefatos de software desenvolvidos para o estudo acadêmico **"Kotlin Multiplatform no Desenvolvimento Mobile: Comparativo de Paridade Técnica e Eficiência frente à Abordagem Nativa"**, apresentado ao Instituto de Ciências Exatas e Informática da PUC Minas como requisito parcial para obtenção do título de Bacharel em Sistemas de Informação.

## Descrição do Estudo
O objetivo deste projeto foi avaliar a eficiência computacional do ecossistema *Kotlin Multiplatform* (KMP) e *Compose Multiplatform* (CMP) em comparação com o desenvolvimento nativo (Android/Kotlin e iOS/Swift). O estudo focou em três pilares de desempenho:
1. **Cold Start:** Latência de inicialização.
2. **Processamento (CPU Bound):** Ordenação de 10.000 registros.
3. **Renderização:** Consumo de RAM e estabilidade de FPS em listas complexas.

## Estrutura do Repositório
* `/data`: Contém o contrato de dados (`produtos.json`) utilizado em todos os testes.
* `/src/android-native`: Código fonte do artefato nativo Android (Kotlin/Jetpack Compose).
* `/src/ios-native`: Código fonte do artefato nativo iOS (Swift/SwiftUI).
* `/src/kmp-shared`: Módulo lógico compartilhado (KMP) e interface unificada (CMP).
* `/scripts`: Ferramentas auxiliares para automação do protocolo de teste.

## Reprodutibilidade
Para garantir a integridade dos dados publicados no artigo, todos os artefatos aqui presentes estão configurados em **Modo Release** (sem *debug logs* ou *debuggers* anexados).

### Como validar os resultados:
Para replicar o *benchmarking* reportado nas Tabelas 1, 2 e 3 do artigo:
1. Utilize um ambiente macOS compatível (especificado no Quadro 1 do artigo).
2. Execute os testes utilizando o **Android Studio Profiler** (para Android) e o **Xcode Instruments** (para iOS).
3. Siga o protocolo descrito na **Seção 4.2** do artigo (reboot forçado do emulador antes de cada um dos 30 ciclos de coleta).

## Fragmentos de Código
Os trechos de código mais relevantes para a análise arquitetural, conforme citados no artigo, podem ser encontrados nas respectivas pastas de cada artefato. A lógica central de ordenação (*CPU Bound*) está centralizada no módulo `kmp-shared`.

---
*Este estudo foi realizado por Robson Nunes de Souza sob orientação da Profa. Maria Ines Lage de Paula (PUC Minas).*

## Citação
Se utilizar este código ou os dados deste estudo em trabalhos acadêmicos, por favor, cite o artigo original.

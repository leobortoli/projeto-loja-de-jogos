using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
public record ProdutoDto(
    [property: JsonPropertyName("id_produto")][Required(ErrorMessage = "O id é obrigatório")]
    string IdProduto,
    [property: JsonPropertyName("nome")][Required(ErrorMessage = "O nome é obrigatório")]
    string Nome,
    string Descricao,
    [property: JsonPropertyName("preco")][Range(0.01, 1000000, ErrorMessage = "O preço deve ser maior que zero")]
    decimal Preco,
    [property: JsonPropertyName("estoque")][Range(0, int.MaxValue, ErrorMessage = "O estoque não pode ser negativo")]
    int Estoque,
    [property: JsonPropertyName("categoria")][Required(ErrorMessage = "A categoria é obrigatória")]
    string Categoria,
    [property: JsonPropertyName("detalhes")] 
    Dictionary<string, object> Detalhes
);
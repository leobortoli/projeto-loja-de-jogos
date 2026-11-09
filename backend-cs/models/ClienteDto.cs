using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
public record ClienteDto(
    [property: JsonPropertyName("id_cliente")][Required(ErrorMessage = "O id é obrigatório")]
    string IdCliente,
    [property: JsonPropertyName("nome")][Required(ErrorMessage = "O nome é obrigatório")]
    string Nome,
    [property: JsonPropertyName("email")]
    string Email,
    [property: JsonPropertyName("cpf")][StringLength(9, ErrorMessage = "O cpf deve ter 9 dígitos")]
    decimal Cpf,
    [property: JsonPropertyName("senha")][Required(ErrorMessage = "A senha é obrigatória")]
    string Senha
);
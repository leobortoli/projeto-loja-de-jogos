[ApiController]
[Route("api/usuarios")]
public class UsuarioController : ControllerBase
{
    private readonly HttpClient _httpClient;
    public UsuarioController(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }
    [HttpPost]
    public async Task<IActionResult> CriarUsuario([FromBody] UsuarioDto dto)
    {
        var response = await _httpClient.PostAsJsonAsync("http://localhost:8000/db/usuarios", dto);
        if (!response.IsSuccessStatusCode)
            return StatusCode(500, "Erro ao salvar no banco de dados.");
        return Ok(new { mensagem = "Usuário processado e salvo com sucesso!" });
    }
}
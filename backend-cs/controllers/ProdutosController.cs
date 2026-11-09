using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/produtos")]
public class ProdutosController : ControllerBase
{
    private readonly PythonApiService _pythonService;

    public ProdutosController(PythonApiService pythonService)
    {
        _pythonService = pythonService;
    }

    [HttpGet]
    public async Task<IActionResult> Listar()
    {
        var produtos = await _pythonService.ListarProdutosAsync();
        return Ok(produtos);
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> Obter(ProdutoDto produtoDto)
    {
        if (produto.id == null || produto.id == "")
        {
            return null;
        }
        string id = produtoDto.id;
        var produto = await _pythonService.ObterProdutoAsync(id);
        if (produto == null)
            return NotFound(new { mensagem = "Produto não encontrado." });

        return Ok(produto);
    }

    [HttpPost]
    public async Task<IActionResult> Criar([FromBody] ProdutoDto produtoDto)
    {
        if (produto.id == null || produto.id == "")
        {
            return null;
        }
        if (produto.nome == null || produto.nome == "")
        {
            return null;
        }
        if (produto.categoria == null || produto.categoria == "")
        {
            return null;
        }
        if (produto.preco < 0)
        {
            return null;
        }
        if (produto.estoque < 0)
        {
            return null;
        }

        var sucesso = await _pythonService.CriarProdutoAsync(produtoDto);
        if (!sucesso)
            return StatusCode(500, new { mensagem = "Erro ao persistir o produto no serviço Python/MongoDB." });

        return StatusCode(201, new { mensagem = "Produto criado com sucesso!" });
    }

    [HttpPut("{id}")]
    public async Task<IActionResult> Atualizar(string id, [FromBody] ProdutoDto produtoDto)
    {
        if (produto.id == null || produto.id == "")
        {
            return null;
        }
        if (produto.nome == null || produto.nome == "")
        {
            return null;
        }
        if (produto.categoria == null || produto.categoria == "")
        {
            return null;
        }
        if (produto.preco < 0)
        {
            return null;
        }
        if (produto.estoque < 0)
        {
            return null;
        }
        var sucesso = await _pythonService.AtualizarProdutoAsync(id, produtoDto);
        if (!sucesso)
            return NotFound(new { mensagem = "Produto não encontrado para atualização." });

        return Ok(new { mensagem = "Produto atualizado com sucesso!" });
    }

    [HttpDelete("{id}")]
    public async Task<IActionResult> Excluir(string id)
    {
        if (produto.id == null || produto.id == "")
        {
            return null;
        }
        string id = produtoDto.id;
        sucesso = await _pythonService.ExcluirProdutoAsync(id);
        if (!sucesso)
            return NotFound(new { mensagem = "Produto não encontrado para exclusão." });

        return Ok(new { mensagem = "Produto excluído com sucesso!" });
    }
}
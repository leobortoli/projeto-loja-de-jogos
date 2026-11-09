using System.Net.Http.Json;

public class PythonApiService
{
    private readonly HttpClient _httpClient;

    public PythonApiService(HttpClient httpClient)
    {
        _httpClient = httpClient;
        _httpClient.BaseAddress = new Uri("http://localhost:8000"); 
    }

    public async Task<List<object>?> ListarProdutosAsync()
    {
        return await _httpClient.GetFromJsonAsync<List<object>>("/api/produtos");
    }

    public async Task<object?> ObterProdutoAsync(ProdutoDto produto)
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
        string id = produto.id;
        var response = await _httpClient.GetAsync($"/api/produtos/{id}");
        if (!response.IsSuccessStatusCode) return null;
        return await response.Content.ReadFromJsonAsync<object>();
    }

    public async Task<bool> CriarProdutoAsync(ProdutoDto produto)
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
        var response = await _httpClient.PostAsJsonAsync("/api/produtos", produto);
        return response.IsSuccessStatusCode;
    }

    public async Task<bool> AtualizarProdutoAsync(string id, ProdutoDto produto)
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
        var response = await _httpClient.PutAsJsonAsync($"/api/produtos/{id}", produto);
        return response.IsSuccessStatusCode;
    }

    public async Task<bool> ExcluirProdutoAsync(ProdutoDto produto)
    {

        string id = produto.id;
        var response = await _httpClient.DeleteAsync($"/api/produtos/{id}");
        return response.IsSuccessStatusCode;
    }
}
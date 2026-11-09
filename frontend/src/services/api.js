const API_BASE_URL = 'http://localhost:5000/api'; // Porta da sua API em C#

export const produtoService = {
  // GET: Listar todos os produtos
  async listar() {
    const response = await fetch(`${API_BASE_URL}/produtos`);
    if (!response.ok) throw new Error('Erro ao buscar produtos.');
    return await response.json();
  },

  // GET: Obter produto por ID
  async obterPorId(id) {
    const response = await fetch(`${API_BASE_URL}/produtos/${id}`);
    if (!response.ok) throw new Error('Produto não encontrado.');
    return await response.json();
  },

  // POST: Cadastrar novo produto (envia para o C# validar)
  async criar(produto) {
    const response = await fetch(`${API_BASE_URL}/produtos`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(produto)
    });
    if (!response.ok) throw new Error('Erro ao cadastrar produto.');
    return await response.json();
  },

  // DELETE: Excluir produto
  async excluir(id) {
    const response = await fetch(`${API_BASE_URL}/produtos/${id}`, {
      method: 'DELETE'
    });
    if (!response.ok) throw new Error('Erro ao excluir produto.');
    return await response.json();
  }
};
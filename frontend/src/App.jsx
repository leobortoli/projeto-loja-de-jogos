import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import ProdutoCard from './components/ProdutoCard';
import { produtoService } from './services/api'; // Importa a service que criamos

export default function App() {
  const [produtos, setProdutos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);
  const [cartCount, setCartCount] = useState(0);

  // useEffect para buscar os dados usando a camada de serviço
  useEffect(() => {
    produtoService.listar()
      .then(data => {
        setProdutos(data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setErro('Não foi possível carregar os produtos do servidor.');
        setLoading(false);
      });
  }, []);

  return (
    <div>
      <Navbar cartCount={cartCount} />
      <div className="container my-5">
        <h2 className="text-center mb-4">Nossos Produtos (Do Banco de Dados)</h2>

        {/* Indicador de Carregamento */}
        {loading && (
          <div className="text-center my-5">
            <div className="spinner-border text-primary" role="status">
              <span className="visually-hidden">Carregando...</span>
            </div>
            <p className="mt-2 text-muted">Buscando produtos no MongoDB...</p>
          </div>
        )}

        {/* Mensagem de Erro caso a API C# ou Python caiam */}
        {erro && (
          <div className="alert alert-danger text-center" role="alert">
            {erro}
          </div>
        )}

        {/* Lista de Cards gerados dinamicamente */}
        {!loading && !erro && (
          <div className="row g-4">
            {produtos.length === 0 ? (
              <p className="text-center text-muted">Nenhum produto cadastrado no momento.</p>
            ) : (
              produtos.map(produto => (
                <ProdutoCard 
                  key={produto.id || produto._id} // Suporta o ID gerado pelo MongoDB
                  produto={{
                    ...produto,
                    // Formata o preço numérico vindo do banco (ex: 4999.9 -> R$ 4.999,90)
                    preco: `R$ ${produto.preco.toLocaleString('pt-BR', { minimumFractionDigits: 2 })}`,
                    // Atribui uma imagem padrão caso o banco não venha com o campo img
                    img: produto.img || "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=500&q=80"
                  }} 
                  onAdicionarAoCarrinho={() => setCartCount(prev => prev + 1)} 
                />
              ))
            )}
          </div>
        )}
      </div>
    </div>
  );
}
import React, { useState } from 'react';

export default function ProdutoCard({ produto, onAdicionarAoCarrinho }) {
  const [favorito, setFavorito] = useState(false);

  return (
    <div className="col-12 col-md-6 col-lg-4">
      <div className="card h-100 shadow-sm">
        <img 
          src={produto.img} 
          className="card-img-top" 
          style={{ height: '200px', objectFit: 'cover' }} 
          alt={produto.nome} 
        />
        <div className="card-body d-flex flex-column">
          <h5 className="card-title">{produto.nome}</h5>
          <p className="card-text text-muted">{produto.preco}</p>
          <div className="mt-auto d-flex gap-2">
            <button
              className={favorito ? 'btn btn-danger' : 'btn btn-outline-danger'}
              onClick={() => setFavorito(!favorito)}
            >
              {favorito ? '♥ Favorito' : '♡ Favoritar'}
            </button>
            <button onClick={onAdicionarAoCarrinho} className="btn btn-primary flex-grow-1">
              <i className="bi bi-plus-circle me-1"></i> Adicionar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
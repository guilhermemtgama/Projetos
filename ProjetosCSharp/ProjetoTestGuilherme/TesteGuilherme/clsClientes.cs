using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TesteGuilherme
{
    public class clsClientes
    {
        private clsClientes() { }
        public clsClientes(int iD, string? nome, string? cpf, string? telefone, string? sexo, string? nascionalidade, DateTime dataNascimento, DateTime dataCadastro)
        {
            ID = iD;
            Nome = nome;
            Cpf = cpf;
            Telefone = telefone;
            Sexo = sexo;
            Nascionalidade = nascionalidade;
            DataNascimento = dataNascimento;
            DataCadastro = dataCadastro;
        }

        public int ID { get; private set; }
        public string? Nome { get; private set; }
        public string? Cpf { get; private set; }
        public string? Telefone {  get; private set; }
        public string? Sexo { get; private set; }
        public string? Nascionalidade { get; private set; }
        public DateTime DataNascimento { get; private set; }
        public DateTime DataCadastro {  get; private set; } 

    }
}

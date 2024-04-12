using Microsoft.VisualBasic.ApplicationServices;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TesteGuilherme.Repositorios
{
    public class clsConexao : IDisposable
    {
        private readonly IDbConnection connection;
        public clsConexao()
        {
            connection = new SqlConnection(@"Server = GUILHERME\SQLEXPRESS; Database = TesteGuilherme; User Id = userguilherme; Password = teste2024;");
        }

        public IDbConnection GetConnetion()
        {
            if (connection.State != ConnectionState.Open)
                connection.Open();
            return connection;
        }
        public void Dispose()
        {
            connection?.Dispose();
        }
    }
}

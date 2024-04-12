
namespace TesteGuilherme
{
    partial class frmCadastroClientes
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            Clientes = new GroupBox();
            txtTelefone = new MaskedTextBox();
            msdDataNascimento = new MaskedTextBox();
            this.lstNacionalidade = new ListBox();
            cmdRemover = new Button();
            cmdEditar = new Button();
            cmdSalvar = new Button();
            label10 = new Label();
            label9 = new Label();
            txtDataCadastro = new TextBox();
            label7 = new Label();
            txtSexo = new TextBox();
            label6 = new Label();
            label5 = new Label();
            txtID = new TextBox();
            label3 = new Label();
            txtCpf = new TextBox();
            label2 = new Label();
            label1 = new Label();
            txtNome = new TextBox();
            grClientes = new DataGridView();
            Clientes.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)grClientes).BeginInit();
            SuspendLayout();
            // 
            // Clientes
            // 
            Clientes.Controls.Add(txtTelefone);
            Clientes.Controls.Add(msdDataNascimento);
            Clientes.Controls.Add(this.lstNacionalidade);
            Clientes.Controls.Add(cmdRemover);
            Clientes.Controls.Add(cmdEditar);
            Clientes.Controls.Add(cmdSalvar);
            Clientes.Controls.Add(label10);
            Clientes.Controls.Add(label9);
            Clientes.Controls.Add(txtDataCadastro);
            Clientes.Controls.Add(label7);
            Clientes.Controls.Add(txtSexo);
            Clientes.Controls.Add(label6);
            Clientes.Controls.Add(label5);
            Clientes.Controls.Add(txtID);
            Clientes.Controls.Add(label3);
            Clientes.Controls.Add(txtCpf);
            Clientes.Controls.Add(label2);
            Clientes.Controls.Add(label1);
            Clientes.Controls.Add(txtNome);
            Clientes.Location = new Point(6, 0);
            Clientes.Name = "Clientes";
            Clientes.Size = new Size(402, 324);
            Clientes.TabIndex = 0;
            Clientes.TabStop = false;
            Clientes.Text = "Clientes";
            Clientes.Enter += groupBox1_Enter;
            // 
            // txtTelefone
            // 
            txtTelefone.Location = new Point(6, 181);
            txtTelefone.Mask = "(99)0000-0000";
            txtTelefone.Name = "txtTelefone";
            txtTelefone.Size = new Size(150, 23);
            txtTelefone.TabIndex = 26;
            // 
            // msdDataNascimento
            // 
            msdDataNascimento.Location = new Point(170, 93);
            msdDataNascimento.Mask = "00/00/0000";
            msdDataNascimento.Name = "msdDataNascimento";
            msdDataNascimento.Size = new Size(150, 23);
            msdDataNascimento.TabIndex = 25;
            msdDataNascimento.ValidatingType = typeof(DateTime);
            msdDataNascimento.MaskInputRejected += maskedTextBox1_MaskInputRejected;
            // 
            // lstNacionalidade
            // 
            this.lstNacionalidade.FormattingEnabled = true;
            this.lstNacionalidade.ItemHeight = 15;
            this.lstNacionalidade.Location = new Point(170, 49);
            this.lstNacionalidade.Name = "lstNacionalidade";
            this.lstNacionalidade.Size = new Size(150, 19);
            this.lstNacionalidade.TabIndex = 24;
            // 
            // cmdRemover
            // 
            cmdRemover.Location = new Point(219, 231);
            cmdRemover.Name = "cmdRemover";
            cmdRemover.Size = new Size(75, 23);
            cmdRemover.TabIndex = 23;
            cmdRemover.Text = "Remover";
            cmdRemover.UseVisualStyleBackColor = true;
            // 
            // cmdEditar
            // 
            cmdEditar.Location = new Point(116, 231);
            cmdEditar.Name = "cmdEditar";
            cmdEditar.Size = new Size(75, 23);
            cmdEditar.TabIndex = 22;
            cmdEditar.Text = "Editar";
            cmdEditar.UseVisualStyleBackColor = true;
            // 
            // cmdSalvar
            // 
            cmdSalvar.Location = new Point(6, 231);
            cmdSalvar.Name = "cmdSalvar";
            cmdSalvar.Size = new Size(75, 23);
            cmdSalvar.TabIndex = 1;
            cmdSalvar.Text = "Salvar";
            cmdSalvar.UseVisualStyleBackColor = true;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Location = new Point(167, 75);
            label10.Name = "label10";
            label10.Size = new Size(98, 15);
            label10.TabIndex = 21;
            label10.Text = "Data Nascimento";
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Location = new Point(170, 119);
            label9.Name = "label9";
            label9.Size = new Size(81, 15);
            label9.TabIndex = 19;
            label9.Text = "Data Cadastro";
            label9.Click += label9_Click;
            // 
            // txtDataCadastro
            // 
            txtDataCadastro.Location = new Point(170, 137);
            txtDataCadastro.Name = "txtDataCadastro";
            txtDataCadastro.Size = new Size(150, 23);
            txtDataCadastro.TabIndex = 18;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Location = new Point(170, 163);
            label7.Name = "label7";
            label7.Size = new Size(32, 15);
            label7.TabIndex = 15;
            label7.Text = "Sexo";
            // 
            // txtSexo
            // 
            txtSexo.Location = new Point(170, 181);
            txtSexo.Name = "txtSexo";
            txtSexo.Size = new Size(150, 23);
            txtSexo.TabIndex = 14;
            txtSexo.TextChanged += txtSexo_TextChanged;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(170, 31);
            label6.Name = "label6";
            label6.Size = new Size(83, 15);
            label6.TabIndex = 13;
            label6.Text = "Nacionalidade";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(6, 31);
            label5.Name = "label5";
            label5.Size = new Size(18, 15);
            label5.TabIndex = 9;
            label5.Text = "ID";
            // 
            // txtID
            // 
            txtID.Enabled = false;
            txtID.Location = new Point(6, 49);
            txtID.Name = "txtID";
            txtID.Size = new Size(150, 23);
            txtID.TabIndex = 8;
            txtID.TextChanged += txtID_TextChanged;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(6, 119);
            label3.Name = "label3";
            label3.Size = new Size(26, 15);
            label3.TabIndex = 5;
            label3.Text = "Cpf";
            // 
            // txtCpf
            // 
            txtCpf.Location = new Point(6, 137);
            txtCpf.Name = "txtCpf";
            txtCpf.Size = new Size(150, 23);
            txtCpf.TabIndex = 4;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(6, 163);
            label2.Name = "label2";
            label2.Size = new Size(51, 15);
            label2.TabIndex = 3;
            label2.Text = "Telefone";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(6, 75);
            label1.Name = "label1";
            label1.Size = new Size(40, 15);
            label1.TabIndex = 1;
            label1.Text = "Nome";
            // 
            // txtNome
            // 
            txtNome.Location = new Point(6, 93);
            txtNome.Name = "txtNome";
            txtNome.Size = new Size(150, 23);
            txtNome.TabIndex = 0;
            txtNome.TextChanged += txtNome_TextChanged;
            // 
            // grClientes
            // 
            grClientes.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            grClientes.Location = new Point(414, 12);
            grClientes.Name = "grClientes";
            grClientes.Size = new Size(374, 312);
            grClientes.TabIndex = 0;
            // 
            // frmCadastroClientes
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 341);
            Controls.Add(grClientes);
            Controls.Add(Clientes);
            Name = "frmCadastroClientes";
            Text = "Teste Guilherme";
            Clientes.ResumeLayout(false);
            Clientes.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)grClientes).EndInit();
            ResumeLayout(false);
        }

        private void label4_Click(object sender, EventArgs e)
        {
            throw new NotImplementedException();
        }

        #endregion

        private GroupBox Clientes;
        private DataGridView grClientes;
        private Label label5;
        private TextBox txtID;
        private Label label3;
        private TextBox txtCpf;
        private Label label2;
        private Label label1;
        private TextBox txtNome;
        private Label label7;
        private TextBox txtSexo;
        private Label label6;
        private Label label10;
        private TextBox txtDataNasimento;
        private Label label9;
        private TextBox txtDataCadastro;
        private Button cmdRemover;
        private Button cmdEditar;
        private Button cmdSalvar;
        private ListBox listBox1;
        private MaskedTextBox msdDataNascimento;
        private MaskedTextBox txtTelefone;
    }
}

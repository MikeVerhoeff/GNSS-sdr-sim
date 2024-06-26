library ieee;
use ieee.std_logic_1164.all;
USE ieee.numeric_std.ALL;
use work.settings.all;

entity InputHandler is
    generic(
        chanel_count : integer := 4
    );
    port(
        clk : in std_logic;
        reset : in std_logic;
        
        serial_in : in std_logic;
        store : in std_logic;

        I : out IQ;
        Q : out IQ;
        debug : out std_logic_vector(7 downto 0)
    );
end InputHandler;

architecture behavioral of InputHandler is

    --constant frameWidth: integer := 176;

    component FIFO
        generic (
          width : integer := frameWidth;
          depth : integer := 10
        );
        port (
          push  : in std_logic;
          pop   : in std_logic;
          reset : in std_logic;
          Q     : in std_logic_vector(frameWidth-1 downto 0);
          D     : out std_logic_vector(frameWidth-1 downto 0)
        );
    end component;

    component Chanel
        port (
          clk : in std_logic;
          reset : in std_logic;
          get_next_frame : out std_logic;
          next_frame : in std_logic_vector(frameWidth-1 downto 0);
          I : out IQ;
          Q : out IQ;
          power : out Power_t
        );
    end component;

    component SPI
        generic (
          n : integer := frameWidth
        );
        port (
          clk : in std_logic;
          reset : in std_logic;
          serial_in : in std_logic;
          parallel_out : out std_logic_vector(n-1 downto 0)
        );
    end component;

    component Mixer
        generic (
          chanel_count : integer := chanel_count
        );
        port (
          clk : in std_logic;
          reset : in std_logic;
          I_s : in IQList;
          Q_s : in IQList;
          powers : in PowerList_t;
          I : out IQ;
          Q : out IQ
        );
    end component;

    component ClockDiv16
      port (
        clk : in std_logic;
        clkdiv : out std_logic
      );
    end component;

    function To_Std_Logic(L: BOOLEAN) return std_ulogic is
    begin
        if L then
            return('1');
        else
            return('0');
        end if;
    end function To_Std_Logic;
    
    
    signal I_s, Q_s : IQList;

    signal power_s : PowerList_t;

    signal push : std_logic_vector(chanel_count-1 downto 0);-- := (others => '0');
    signal pop  : std_logic_vector(chanel_count-1 downto 0) := (others => '0');

    signal newData : std_logic_vector(frameWidth-1 downto 0);
    type Frames_t is array(chanel_count-1 downto 0) of std_logic_vector(frameWidth-1 downto 0);
    signal frames : Frames_t;

    signal chanel_select : integer;
    signal chanel_select_v : std_logic_vector(7 downto 0);

    signal clk16 : std_logic;
    
	 signal I_tmp : IQ;
	 
	 --constant g : integer := 0;
begin

    chanel_select <= to_integer(unsigned(newData(frameWidth-1 downto frameWidth-8)));
    chanel_select_v <= newData(frameWidth-1 downto frameWidth-8);

    --debug <= chanel_select_v;
    --debug <= std_logic_vector(I_tmp);
	 I <= I_tmp;
	 debug <= push(0) & pop(0) & newData(3 downto 2) & chanel_select_v(3 downto 0);

    SPI_IN: SPI port map (clk, reset, serial_in, newData);

    CLK_DIV : ClockDiv16 port map (clk, clk16);

    GEN_CHANEL:
    for g in 0 to chanel_count-1 generate
        FIFO_X: FIFO port map (push(g), pop(g), reset, newData, frames(g));
        CHANEL_X: Chanel port map (clk16, reset, pop(g), frames(g), I_s(g), Q_s(g), power_s(g));
        push(g) <= To_Std_Logic( (store='1') and (chanel_select=g) );
    end generate GEN_CHANEL;

    RESULT: Mixer port map(clk16, reset, I_s, Q_s, power_s, I_tmp, Q);

end architecture;
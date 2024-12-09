from dlms_cosem import a_xdr, cosem, enumerations, utils
from dlms_cosem.security import (
    
    NoSecurityAuthentication,
    HighLevelSecurityGmacAuthentication,
    
    LowLevelSecurityAuthentication,
)
from dlms_cosem.client import DlmsClient
from dlms_cosem.io import SerialIO, HdlcTransport,TcpTransport, BlockingTcpIO
from .models import Meter
import logging



logger = logging.getLogger('dlsm_cosem')
logger.setLevel(logging.INFO)
logging.basicConfig(filename='mi_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def simple_de_medidor(medidor):
    if medidor.con_method.type == 'TCP':
        tcp_io = BlockingTcpIO(host=medidor.con_ip, port=medidor.con_port)
        tcp_transport = TcpTransport(
            io=tcp_io,
            client_logical_address=16,
            server_logical_address=1, 
            server_physical_address=17,)
        tcp_transport_m = TcpTransport(
            io=tcp_io,
            client_logical_address=1,
            server_logical_address=1, 
            server_physical_address=17,)
        
        public_client = DlmsClient(transport=tcp_transport, 
                        authentication=NoSecurityAuthentication())
        management_client = DlmsClient(
            transport=tcp_transport_m,
            authentication=LowLevelSecurityAuthentication(secret=b'ABCDEFGH'),
        )
    elif medidor.con_method.type == 'HDLC_IP':
        tcp_io = BlockingTcpIO(host=medidor.con_ip, port=medidor.con_port)
        tcp_transport = HdlcTransport(
            io=tcp_io,
            client_logical_address=16,
            server_logical_address=1, 
            server_physical_address=17,)
        tcp_transport_m = HdlcTransport(
            io=tcp_io,
            client_logical_address=1,
            server_logical_address=1, 
            server_physical_address=17,)
        
        public_client = DlmsClient(transport=tcp_transport, 
                        authentication=NoSecurityAuthentication())
        management_client = DlmsClient(
            transport=tcp_transport_m,
            authentication=LowLevelSecurityAuthentication(secret=b'ABCDEFGH'),
        )
    else: 
        port = medidor.con_port
        serial_io = SerialIO(port_name=port, baud_rate=medidor.baud_rate)

        public_hdlc_transport = HdlcTransport(
            client_logical_address=16,
            server_logical_address=1,
            server_physical_address=17,
            io=serial_io,
        )
        public_hdlc_transport_m = HdlcTransport(
            client_logical_address=1,
            server_logical_address=1,
            server_physical_address=17,
            io=serial_io,
        )
        public_client = DlmsClient(
            transport=public_hdlc_transport, 
            authentication=NoSecurityAuthentication()
        )
        management_client = DlmsClient(
            transport=public_hdlc_transport_m,
            authentication=LowLevelSecurityAuthentication(secret=b'ABCDEFGH'),
        )


    def reg_obi(obi):
        cosem.CosemAttribute(
                interface=enumerations.CosemInterface.REGISTER,
                instance=cosem.Obis(obi),
                attribute=2,
                
            )
    
    with public_client.session() as client:
        
        # COSEM_logical_device_name-----------------------------------------------------
        response_data = client.get(
            cosem.CosemAttribute(
                interface=enumerations.CosemInterface.DATA,
                instance=cosem.Obis(0, 0, 42, 0, 0),
                attribute=2,
                
            )
        )
        data_decoder = a_xdr.AXdrDecoder(
            encoding_conf=a_xdr.EncodingConf(
                attributes=[a_xdr.Sequence(attribute_name="data")]
            )
        )
        
        COSEM_logical_device_name = data_decoder.decode(response_data)["data"]
        print(f"COSEM_logical_device_name = {COSEM_logical_device_name}")
    
    # Lecturas con privilegios----------------------------------------------
    
    with management_client.session() as client:
        pot_act_dir = utils.parse_as_dlms_data(client.get(
            cosem.CosemAttribute(
                interface=enumerations.CosemInterface.REGISTER,
                instance=cosem.Obis(1, 1, 1, 7, 0),
                attribute=2,)
        ))
        
        pot_act_rev = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 2, 7, 0),
            attribute=2,)
            ))
        
        pot_reac_cap_QI = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 5, 7, 0),
            attribute=2,)
            ))
        pot_reac_cap_QII = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 6, 7, 0),
            attribute=2,)
            ))
        pot_reac_cap_QIII = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 7, 7, 0),
            attribute=2,)
            ))
        pot_reac_cap_QIV = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 8, 7, 0),
            attribute=2,)
            ))
        pot_apar_dir = utils.parse_as_dlms_data(client.get(
            cosem.CosemAttribute(
                interface=enumerations.CosemInterface.REGISTER,
                instance=cosem.Obis(1, 1, 9, 7, 0),
                attribute=2,)
        ))
        
        pot_apar_rev = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 10, 7, 0),
            attribute=2,)
            ))
        
        vol_de_fase_1 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 32, 7, 0),
            attribute=2,)
            ))
        
        vol_de_fase_2 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 52, 7, 0),
            attribute=2,)
            ))
        
        vol_de_fase_3 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 72, 7, 0),
            attribute=2,)
            ))
        corriente_1 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 31, 7, 0),
            attribute=2,)
            ))
        corriente_2 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 51, 7, 0),
            attribute=2,)
            ))
        corriente_3 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 71, 7, 0),
            attribute=2,)
            ))
        fact_de_pot = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 13, 7, 0),
            attribute=2,)
            ))
        fact_de_pot_1 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 33, 7, 0),
            attribute=2,)
            ))
        fact_de_pot_2 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 53, 7, 0),
            attribute=2,)
            ))
        fact_de_pot_3 = utils.parse_as_dlms_data(client.get(
        cosem.CosemAttribute(
            interface=enumerations.CosemInterface.REGISTER,
            instance=cosem.Obis(1, 1, 73, 7, 0),
            attribute=2,)
            ))
        
    medidor.logical_name = COSEM_logical_device_name
    medidor.pot_act_dir = pot_act_dir
    medidor.pot_act_rev = pot_act_rev
    medidor.pot_reac_cap_QI =pot_reac_cap_QI
    medidor.pot_reac_cap_QII =pot_reac_cap_QII
    medidor.pot_reac_cap_QIII =pot_reac_cap_QIII
    medidor.pot_reac_cap_QIV =pot_reac_cap_QIV
    medidor.pot_apar_dir = pot_apar_dir
    medidor.pot_apar_rev = pot_apar_rev
    medidor.vol_de_fase_1 = vol_de_fase_1
    medidor.vol_de_fase_2 = vol_de_fase_2
    medidor.vol_de_fase_3 = vol_de_fase_3
    medidor.corriente_1 = corriente_1
    medidor.corriente_2 = corriente_2
    medidor.corriente_3 = corriente_3
    medidor.fact_de_pot = fact_de_pot
    medidor.fact_de_pot_1 = fact_de_pot_1
    medidor.fact_de_pot_2 = fact_de_pot_2
    medidor.fact_de_pot_3 = fact_de_pot_3
    
    return medidor

def lectura_global():
    medidores = Meter.objects.all()
    for medidor in medidores:
        try:
            medidor_leido = simple_de_medidor(medidor)
            medidor_leido.save()
        except:
            print('Falla lectura de: ', medidor.name)
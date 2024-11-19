import pandapower as pp
import pandas as pd


def create_network(net):
    hb1 = pp.create_bus(net, vn_kv=35., name="ZRU-2.2-1s")
    lb1 = pp.create_bus(net, vn_kv=0.4, name="Выводы 0,4 кВ Трансформатора")
    pp.create_transformer(net, hv_bus=hb1, lv_bus=lb1, name="T1", in_service=True, max_loading_percent=120,
                          vk_percent_characteristic=6,
                          std_type="2.5 MVA 35/0.4 kV"
                          )

    lb2 = pp.create_bus(net, vn_kv=0.4, name="в конце шинопровода")
    lb3 = pp.create_bus(net, vn_kv=0.4, name="AKFA")
    lb4 = pp.create_bus(net, vn_kv=0.4, name="стройка")

    pp.create_line(net, from_bus=lb1, to_bus=lb2, length_km=0.27, std_type="BUSDUCT 3100A", name="BUSDUCT")
    pp.create_line(net, from_bus=lb2, to_bus=lb3, length_km=0.13, std_type="ВВГНГ-4x240-1", parallel=5,
                   name="CABLE_AKFA")
    pp.create_line(net, from_bus=lb2, to_bus=lb4, length_km=0.27, std_type="ВВГНГ-4x240-1", name="CABLE_SITE")

    pp.create_load(net, bus=lb3, p_mw=1.56, q_mvar=.310)
    pp.create_load(net, bus=lb4, p_mw=0.3, q_mvar=.158)

    pp.create_ext_grid(net, bus=hb1, vm_pu=1.1, s_sc_max_mva=497.3, s_sc_min_mva=116.6, rx_max=0.2)

    pp.runpp(net)

    pp.shortcircuit.calc_sc(net, bus=None, fault='3ph', case='max', lv_tol_percent=10, topology='auto',
                            ip=False, ith=False, tk_s=1.0, kappa_method='C', r_fault_ohm=0.0, x_fault_ohm=0.0,
                            branch_results=False, check_connectivity=True, return_all_currents=False,
                            inverse_y=True, use_pre_fault_voltage=False)

    return net


def create_lines(net):
    APVPU_1_150_35 = {
        'c_nf_per_km': 175,
        'r_ohm_per_km': 0.206,
        'x_ohm_per_km': 0.13,
        'max_i_ka': 14.2,
        'name': "АПВПУ-1x150-35"
    }

    BUSDUCT_3100_04 = {
        'c_nf_per_km': 200,
        'r_ohm_per_km': 0.017,
        'x_ohm_per_km': 0.009,
        'max_i_ka': 72,
        'name': "BUSDUCT 3100A"
    }

    VVGNG_4_240_1 = {
        'c_nf_per_km': 300,
        'r_ohm_per_km': 0.15,
        'x_ohm_per_km': 0.08,
        'max_i_ka': 26.8,
        'name': "ВВГНГ-4x240-1"
    }

    for data in [APVPU_1_150_35, BUSDUCT_3100_04, VVGNG_4_240_1]:
        pp.create_std_type(net, data, data['name'], element='line', overwrite=True, check_required=True)

    return net


def create_trafo(net):
    pp.create_std_type(net, {"sn_mva": 2.5,
                             "vn_hv_kv": 35,
                             "vn_lv_kv": 0.4,
                             "vk_percent": 6,
                             "vkr_percent": 0.78125,
                             "pfe_kw": 2.7,
                             "i0_percent": 0.16875,
                             "shift_degree": 0,
                             "vector_group": "Dyn",
                             "tap_side": "hv",
                             "tap_neutral": 0,
                             "tap_min": -2,
                             "tap_max": 2,
                             "tap_step_degree": 0,
                             "tap_step_percent": 2.5,
                             "tap_phase_shifter": False,
                             "vk0_percent": 6,
                             "vkr0_percent": 0.78125,
                             "mag0_percent": 100,
                             "mag0_rx": 0.,
                             "si0_hv_partial": 0.9, }, name='2.5 MVA 35/0.4 kV', element="trafo")
    return net


def show_results(c_net):
    attrs = ['OPF_converged', '_empty_res_asymmetric_load', '_empty_res_asymmetric_load_3ph',
             '_empty_res_asymmetric_sgen',
             '_empty_res_asymmetric_sgen_3ph', '_empty_res_bus', '_empty_res_bus_3ph', '_empty_res_dcline',
             '_empty_res_ext_grid',
             '_empty_res_ext_grid_3ph', '_empty_res_gen', '_empty_res_impedance', '_empty_res_line',
             '_empty_res_line_3ph',
             '_empty_res_load', '_empty_res_load_3ph', '_empty_res_motor', '_empty_res_protection', '_empty_res_sgen',
             '_empty_res_sgen_3ph', '_empty_res_shunt', '_empty_res_ssc', '_empty_res_storage',
             '_empty_res_storage_3ph',
             '_empty_res_svc', '_empty_res_switch', '_empty_res_tcsc', '_empty_res_trafo', '_empty_res_trafo3w',
             '_empty_res_trafo_3ph', '_empty_res_ward', '_empty_res_xward', '_gen_order', '_impedance_bb_switches',
             '_is_elements', '_is_elements_final', '_isolated_buses', '_options', '_pd2ppc_lookups', '_ppc', '_ppc0',
             '_ppc1', '_ppc2', 'asymmetric_load', 'asymmetric_sgen', 'bus', 'bus_geodata', 'characteristic',
             'controller',
             'converged', 'dcline', 'ext_grid', 'f_hz', 'format_version', 'gen', 'group', 'impedance', 'line',
             'line_geodata',
             'load', 'measurement', 'motor', 'name', 'poly_cost', 'pwl_cost', 'res_asymmetric_load',
             'res_asymmetric_load_3ph',
             'res_asymmetric_sgen', 'res_asymmetric_sgen_3ph', 'res_bus', 'res_bus_3ph', 'res_bus_est', 'res_bus_sc',
             'res_dcline',
             'res_ext_grid', 'res_ext_grid_3ph', 'res_ext_grid_sc', 'res_gen', 'res_gen_sc', 'res_impedance',
             'res_impedance_est',
             'res_line', 'res_line_3ph', 'res_line_est', 'res_line_sc', 'res_load', 'res_load_3ph', 'res_motor',
             'res_sgen',
             'res_sgen_3ph', 'res_sgen_sc', 'res_shunt', 'res_shunt_3ph', 'res_ssc', 'res_storage', 'res_storage_3ph',
             'res_svc',
             'res_switch', 'res_switch_est', 'res_switch_sc', 'res_tcsc', 'res_trafo', 'res_trafo3w', 'res_trafo3w_est',
             'res_trafo3w_sc', 'res_trafo_3ph', 'res_trafo_est', 'res_trafo_sc', 'res_ward', 'res_xward', 'sgen',
             'shunt',
             'sn_mva', 'ssc', 'std_types', 'storage', 'svc', 'switch', 'tcsc', 'trafo', 'trafo3w', 'user_pf_options',
             # 'version',
             'ward', 'xward']
    for a in attrs:
        att = getattr(c_net, a)
        try:
            if att is None:
                continue
            if len(att) == 0:
                continue
            print(f"Type: {type(att)}; Name: {a}")
            print("------------------------------------------------------------------------------------------------")
            print(f"{att} \n")
        except Exception as e:
            print(f"Error getting attribute {a}: {e}")


def calculate():
    net = pp.create_empty_network()

    net = create_lines(net)
    net = create_trafo(net)

    c_net = create_network(net)

    voltages_df = c_net.bus
    voltages_df["Voltage_%"] = c_net.res_bus.vm_pu.round(3)
    sc_df = c_net.res_bus_sc
    buses_df = pd.merge(voltages_df, sc_df['ikss_ka'].round(3), left_index=True, right_index=True, how="left")
    buses_df.drop(columns=['zone', 'in_service'], inplace=True)
    # print(voltages_df)
    lines_df = pd.DataFrame()
    lines_df["Line name"] = c_net.line.name
    lines_df["Current, A"] = round(c_net.res_line.i_ka * 1000, 2)

    return buses_df, lines_df

    # print(c_net.res_bus_sc)

    # pp.plotting.simple_plot(c_net, respect_switches=True, line_width=2.0, bus_size=2.0, ext_grid_size=3.0, trafo_size=3.0,
    #                         plot_loads=True, plot_sgens=True, load_size=3.0, sgen_size=1.0, switch_size=2.0,
    #                         switch_distance=1.0, plot_line_switches=True, scale_size=True, bus_color='b',
    #                         line_color='grey', trafo_color='k', ext_grid_color='y', switch_color='k', library='igraph',
    #                         show_plot=True, ax=None)

    # show_results(c_net)

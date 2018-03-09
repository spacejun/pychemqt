#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''Pychemqt, Chemical Engineering Process simulator
Copyright (C) 2009-2017, Juan José Gómez Romera <jjgomera@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.'''


from unittest import TestCase

from lib.meos import MEoS
from lib import unidades


class CH4(MEoS):
    """Multiparameter equation of state for methane"""
    name = "methane"
    CASNumber = "74-82-8"
    formula = "CH4"
    synonym = "R-50"
    rhoc = unidades.Density(162.66)
    Tc = unidades.Temperature(190.564)
    Pc = unidades.Pressure(4599.2, "kPa")
    M = 16.0428  # g/mol
    Tt = unidades.Temperature(90.694)
    Tb = unidades.Temperature(111.667)
    f_acent = 0.01142
    momentoDipolar = unidades.DipoleMoment(0.0, "Debye")
    id = 2
    _Tr = unidades.Temperature(186.659809)
    _rhor = unidades.Density(163.413536)
    _w = 0.010528102

    Fi1 = {"ao_log": [1, 3.00160],
           "pow": [0, 1],
           "ao_pow": [9.91243972, -6.33270087],
           "ao_exp": [0.008449, 4.6942, 3.4865, 1.6572, 1.4115],
           "titao": [648/Tc, 1957/Tc, 3895/Tc, 5705/Tc, 15080/Tc],
           "ao_hyp": [], "hyp": []}

    Fi2 = {"R": 8.314510,
           "ao_log": [1, 3.00088],
           "pow": [0, 1],
           "ao_pow": [19.597508817, -83.959667892],
           "ao_exp": [], "titao": [],
           "ao_hyp": [0.76315, 0.0046, 8.74432, -4.46921],
           "hyp": [4.306474465, 0.936220902, 5.577233895, 5.722644361]}

    Fi3 = {"ao_log": [1, 2.5998324],
           "pow": [0, -1./3, -2./3, -1],
           "ao_pow": [-10.413865, -3.3854083, 1.6900979, -0.3911541],
           "ao_exp": [4.7206715], "titao": [10.543907],
           "ao_hyp": [], "hyp": []}

    CP4 = {"ao": 0.15438149595e2,
           "an": [-0.18044750507e7, 0.77426666393e5, -0.13241658754e4,
                  -0.51479005257e-1, 0.10809172196e-3, -0.65501783437e-7],
           "pow": [-3, -2, -1.001, 1, 2, 3],
           "ao_exp": [-0.67490056171e1], "exp": [3000],
           "ao_hyp": [], "hyp": []}

    setzmann = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for methane of Setzmann and "
                    "Wagner (1991)",
        "__doi__": {"autor": "Setzmann, U., Wagner, W.",
                    "title": "A New Equation of State and Tables of "
                             "Thermodynamic Properties for Methane Covering "
                             "the Range from the Melting Line to 625 K at "
                             "Pressures up to 1000 MPa",
                    "ref": "J. Phys. Chem. Ref. Data, 20(6) (1991) 1061-1155",
                    "doi": "10.1063/1.555898"},

        "R": 8.31451,
        "cp": Fi1,
        "ref": "OTO",

        "Tmin": Tt, "Tmax": 625.0, "Pmax": 1000000.0, "rhomax": 40.072,
        "Pmin": 11.696, "rhomin": 28.142,

        "nr1": [0.43679010280e-1, 0.67092361990, -0.17655778590e01,
                0.85823302410, -0.12065130520e01, 0.51204672200,
                -0.40000107910e-3, -0.12478424230e-1, 0.31002697010e-1,
                0.17547485220e-2, -0.31719216050e-5, -0.22403468400e-5,
                0.29470561560e-6],
        "d1": [1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 8, 9, 10],
        "t1": [-0.5, 0.5, 1., 0.5, 1., 1.5, 4.5, 0., 1., 3., 1., 3., 3.],

        "nr2": [0.18304879090, 0.15118836790, -0.42893638770, 0.68940024460e-1,
                -0.14083139960e-1, -0.30630548300e-1, -0.29699067080e-1,
                -0.19320408310e-1, -0.11057399590, 0.99525489950e-1,
                0.85484378250e-2, -0.61505556620e-1, -0.42917924230e-1,
                -0.18132072900e-1, 0.34459047600e-1, -0.23859194500e-2,
                -0.11590949390e-1, 0.66416936020e-1, -0.23715495900e-1,
                -0.39616249050e-1, -0.13872920440e-1, 0.33894895990e-1,
                -0.29273787530e-2],
        "d2": [1, 1, 1, 2, 4, 5, 6, 1, 2, 3, 4, 4, 3, 5, 5, 8, 2, 3, 4, 4, 4,
               5, 6],
        "t2": [0., 1., 2., 0., 0., 2., 2., 5., 5., 5., 2., 4., 12., 8., 10.,
               10., 10., 14., 12., 18., 22., 18., 14.],
        "c2": [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4,
               4, 4],
        "gamma2": [1]*23,

        "nr3": [9.324799946e-5, -6.287171518,  12.71069467, -6.423953466],
        "d3": [2, 0, 0, 0],
        "t3": [2., 0., 1., 2.],
        "alfa3": [20, 40, 40, 40],
        "beta3": [200, 250, 250, 250],
        "gamma3": [1.07, 1.11, 1.11, 1.11],
        "epsilon3": [1]*4}

    MBWR = {
        "__type__": "MBWR",
        "__name__": "MBWR equation of state for ethane of Younglove and Ely "
                    "(1987)",
        "__doi__": {"autor": "Younglove, B.A. and Ely, J.F.",
                    "title": "Thermophysical Properties of Fluids. II. "
                             "Methane, Ethane, Propane, Isobutane, and Normal "
                             "Butane",
                    "ref": "J. Phys. Chem. Ref. Data 16(4) (1987) 577-798",
                    "doi": "10.1063/1.555785"},

        "Tmin": 90.68, "Tmax": 600.0, "Pmax": 200000.0, "rhomax": 36.2029,
        "Pmin": 11.744, "rhomin": 28.147,

        "R": 8.31434,
        "cp": CP4,
        "ref": {"Tref": 298.15, "Pref": 101.325, "ho": 10018, "so": 186.266},

        "b": [None, 0.9898937956e-4, 0.2199608275, -0.5322788000e1,
              0.2021657962e3, -0.2234398926e5, 0.106794028e-3, 0.1457922469e-2,
              -9.265816666, 0.2915364732e4, 0.2313546209e-5, 0.1387214274e-2,
              0.4780467451e-1, 0.1176103833e-3, -0.198209673e-2, -0.2512887756,
              0.9748899826e-4, -0.1202192137e-5, 0.4128353939e-3,
              -0.7215842918e-5, 0.5081738255e4, -0.9198903192e6, -27.32264677,
              0.7499024351e6, 0.01114060908, 0.1083955159e2, -0.4490960312e-3,
              -0.1380337847e2, -0.2371902232e-6, 0.3761652197e-3,
              -0.2375166954e-8, -0.1237640790e-6, 0.6766926453e-5]}

    GERG = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for methane of Kunz and "
                    "Wagner (2004).",
        "__doi__": {"autor": "Kunz, O., Wagner, W.",
                    "title": "The GERG-2008 Wide-Range Equation of State for "
                             "Natural Gases and Other Mixtures: An Expansion "
                             "of GERG-2004",
                    "ref": "J. Chem.Eng. Data 57(11) (2012) 3032-3091",
                    "doi":  "10.1021/je300655b"},
        "R": 8.314472,
        "cp": Fi2,
        "ref": "OTO",

        "Tmin": 90.6941, "Tmax": 625.0, "Pmax": 1000000.0, "rhomax": 40.072,
        "Pmin": 73.476, "rhomin": 29.249,

        "nr1":  [0.57335704239162, -0.16760687523730e1, 0.23405291834916,
                 -0.21947376343441, 0.16369201404128e-1, 0.15004406389280e-1],
        "d1": [1, 1, 2, 2, 4, 4],
        "t1": [0.125, 1.125, 0.375, 1.125, 0.625, 1.5],

        "nr2": [0.98990489492918e-1, 0.58382770929055, -0.7478686756039,
                0.30033302857974, 0.20985543806568, -0.18590151133061e-1,
                -0.15782558339049, 0.12716735220791, -0.32019743894346e-1,
                -0.68049729364536e-1, 0.24291412853736e-1, 0.51440451639444e-2,
                -0.019084949733532, 0.55229677241291e-2, -0.44197392976085e-2,
                0.040061416708429, -0.33752085907575e-1, -0.25127658213357e-2],
        "d2": [1, 1, 1, 2, 3, 6, 2, 3, 3, 4, 4, 2, 3, 4, 5, 6, 6, 7],
        "t2": [0.625, 2.625, 2.75, 2.125, 2, 1.75, 4.5, 4.75, 5, 4, 4.5, 7.5,
               14, 11.5, 26, 28, 30, 16],
        "c2": [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 6, 6, 6, 6],
        "gamma2": [1]*18}

    friend = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for methane of Friend et al. (1989)",
        "__doi__": {"autor": "Friend, D.G., Ely, J.F., and Ingham, H.",
                    "title": "Thermophysical Properties of Methane",
                    "ref": "J. Phys. Chem. Ref. Data 18, 583 (1989)",
                    "doi": "10.1063/1.555828"},
        "__test__":
            # Table A1, Pag 630
            """
            >>> st=CH4(T=100, P=1e5, eq=3)
            >>> print "%0.6g %0.1f %0.3f %0.3f %0.3f %0.3f %0.2f" % (\
                st.T, st.aM0.kJkmol, st.hM0.kJkmol, st.sM0.kJkmolK, st.cpM0.kJkmolK)
            100 -12.479 3.311 149.58 33.277
            """
            # Table A2, Pag 337
            """
            >>> st=CH4(T=92, x=0.5, eq=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            92 0.014 28.04 0.018 53.37 1532.7 194.89 209.7
            >>> st=CH4(T=100, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            100 0.034 27.35 0.042 54.80 1444.3 156.97 199.5
            >>> st=CH4(T=110, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            110 0.088 26.47 0.100 55.72 1344.7 122.39 186.0
            >>> st=CH4(T=120, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            120 0.192 25.55 0.204 56.68 1245.3 97.85 172.0
            >>> st=CH4(T=130, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            130 0.368 24.56 0.373 58.05 1142.2 79.97 157.8
            >>> st=CH4(T=140, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            140 0.642 23.50 0.633 60.05 1033.3 66.42 143.6
            >>> st=CH4(T=150, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.1e %0.2f %0.2e %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            150 1.041 22.31 1.018 62.98 917.2 55.67 129.3
            >>> st=CH4(T=160, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.3f %0.2f %0.3f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            160 1.593 20.96 1.584 67.42 791.5 46.70 115.0
            >>> st=CH4(T=170, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.3f %0.2f %0.3f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            170 2.329 19.35 2.432 75.04 653.2 38.76 100.5
            >>> st=CH4(T=180, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.3f %0.2f %0.3f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            180 3.287 17.21 3.827 92.96 496.4 31.01 85.5
            >>> st=CH4(T=190, x=0.5, eq=3, visco=3)
            >>> print "%0.6g %0.3f %0.2f %0.3f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.Liquido.rhoM, st.Gas.rhoM, st.Liquido.cpM.JmolK, \
                st.Liquido.w, st.Liquido.mu.muPas, st.Liquido.k.mWmK)
            190 4.521 12.5 7.827 389.9 264.3 19.75 100.3
            """
            # Table A3, Pag 339
            """
            >>> st=CH4(T=100, P=1e5, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            100 0.1 27.37 -5.242 73.05 34.08 54.64 1446.8 157.48 199.8
            >>> st=CH4(T=110, P=1e7, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            110 10 27.01 -4.449 77.13 33.86 54.39 1435.8 137.99 196.6
            >>> st=CH4(T=120, P=2e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            120 2 25.68 -4.084 82.95 32.71 56.59 1268.0 100.43 174.4
            >>> st=CH4(T=130, P=1e7, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            130 10 25.31 -3.348 86.32 32.27 55.81 1258.7 91.19 170.4
            >>> st=CH4(T=140, P=5e7, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            140 50 26.69 -1.866 85.92 33.44 51.40 1496.4 122.21 199.6
            >>> st=CH4(T=160, P=2e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            160 2 21.05 -1.634 100.48 30.52 70.18 804.0 47.23 116.0
            >>> st=CH4(T=180, P=1e5, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            180 0.1 0.07 5.937 169.02 25.18 33.77 350.7 7.01 19.4
            >>> st=CH4(T=200, P=1e7, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            200 10 16.59 1.159 113.68 30.21 84.94 566.0 29.72 84.1
            >>> st=CH4(T=240, P=1e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            240 1 0.52 7.760 159.01 26.08 35.84 398.2 9.36 27.4
            >>> st=CH4(T=270, P=2e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            270 2 0.94 8.641 156.96 26.90 37.46 419.5 10.58 31.9
            >>> st=CH4(T=280, P=5e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            280 5 2.40 8.451 149.22 27.75 42.04 420.0 11.68 36.1
            >>> st=CH4(T=300, P=1e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            300 1 0.41 9.927 167.07 27.61 36.72 447.0 11.35 35.0
            >>> st=CH4(T=330, P=5e5, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            330 0.5 0.18 11.109 176.53 28.76 37.38 468.7 12.21 39.0
            >>> st=CH4(T=360, P=2e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            360 2 0.68 12.083 167.95 30.34 39.67 486.4 13.35 44.4
            >>> st=CH4(T=400, P=5e6, eq=3, visco=3)
            >>> print "%0.6g %0.2g %0.2f %0.3f %0.2f %0.2f %0.2f %0.1f %0.2f %0.1f" % (\
                st.T, st.P.MPa, st.rhoM, st.hM.kJmol, st.sM.JmolK, st.cvM.JmolK, \
                st.cpM.JmolK, st.w, st.mu.muPas, st.k.mWmK)
            400 5 1.53 13.441 164.04 32.65 42.95 512.9 14.96 52.6
            """,

        "R": 8.31451,
        "cp": Fi3,
        "ref": {"Tref": 298.15, "Pref": 101.325, "ho": 10017.7, "so": 186.266},
        "Tt": 90.6854, "Tc": 190.551, "rhoc": 10.139, "M": 16.043,

        "Tmin": Tt, "Tmax": 620.0, "Pmax": 100000.0, "rhomax": 29.714,
        "Pmin": 11.694, "rhomin": 28.145,

        "nr1": [0.384436099659, -0.179692598800e1, 0.329444947369,
                0.226312728442e-1, 0.759236768798e-1, 0.693758447259e-1,
                0.241163263947e-1, 0.107009920854e-1, -0.380933275164e-1,
                0.471537561143e-3, 0.556607678805e-3, 0.548759346533e-6,
                -0.999632699967e-4],
        "d1": [1, 1, 1, 2, 2, 2, 3, 3, 3, 6, 7, 7, 8],
        "t1": [0, 1.5, 2.5, -0.5, 1.5, 2, 0, 1, 2.5, 0, 2, 5, 2],

        "nr2": [-0.128087979280, 0.380198873377e-1, 0.139226650551,
                -0.874996348859e-1, -0.334894165760e-2, -0.517576297122e-1,
                0.252835179116e-1, 0.518703205950e-3, -0.166770594525e-2,
                -0.607401927389e-3, -0.972915359991e-4, -0.298844010462e-4,
                -0.130940111124e-1, 0.198175833798e-1, 0.208465762327e-1,
                -0.358025052631e-1, -0.203486851741, 0.215964755088,
                -0.429340628249e-2],
        "d2": [1, 1, 2, 2, 3, 3, 5, 6, 7, 8, 10, 2, 3, 3, 4, 4, 5, 5, 5],
        "t2": [5, 6, 3.5, 5.5, 3, 7, 6, 8.5, 4, 6.5, 5.5, 22, 11, 18, 11, 23,
               17, 18, 23],
        "c2": [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4, 4],
        "gamma2": [1]*19}

    shortSpan = {
        "__type__": "Helmholtz",
        "__name__": "short Helmholtz equation of state for methane of Span "
                    "and Wagner (2003)",
        "__doi__": {"autor": "Span, R., Wagner, W.",
                    "title": "Equations of state for technical applications. "
                             "II. Results for nonpolar fluids.",
                    "ref": "Int. J. Thermophys. 24 (1) (2003) 41-109",
                    "doi": "10.1023/A:1022310214958"},

        "R": 8.31451,
        "cp": Fi1,
        "ref": "OTO",
        "M": 16.043,

        "Tmin": Tt, "Tmax": 750.0, "Pmax": 100000.0, "rhomax": 40.072,
        "Pmin": 11.661, "rhomin": 28.167,

        "nr1": [0.89269676, -0.25438282e1, 0.64980978, 0.20793471e-1,
                0.70189104e-1, 0.23700378e-3],
        "d1": [1, 1, 1, 2, 3, 7],
        "t1": [0.25, 1.125, 1.5, 1.375, 0.25, 0.875],

        "nr2": [0.16653334, -0.43855669e-1, -0.1572678, -0.35311675e-1,
                -0.29570024e-1, 0.14019842e-1],
        "d2": [2, 5, 1, 4, 3, 4],
        "t2": [0.625, 1.75, 3.625, 3.625, 14.5, 12.],
        "c2": [1, 1, 2, 2, 3, 3],
        "gamma2": [1]*6}

    sun = {
        "__type__": "Helmholtz",
        "__name__": "Helmholtz equation of state for methane of Sun and Ely "
                    "(2004)",
        "__doi__": {"autor": "Sun, L. and Ely, J.F.",
                    "title": "Universal equation of state for engineering "
                             "application: Algorithm and  application to "
                             "non-polar and polar fluids",
                    "ref": "Fluid Phase Equilib., 222-223 (2004) 107-118",
                    "doi": "10.1016/j.fluid.2004.06.028"},
        "R": 8.31451,
        "cp": Fi1,
        "ref": "OTO",

        "Tmin": Tt, "Tmax": 625.0, "Pmax": 1000000.0, "rhomax": 40.072,
        "Pmin": 11.696, "rhomin": 28.142,

        "nr1": [1.25595787, 8.48007435e-1, -3.00939285, 5.99544996e-2,
                2.57003062e-4, -2.85914246e-2],
        "d1": [1, 1, 1, 3, 7, 2],
        "t1": [1.5, 0.25, 1.25, 0.25, 0.875, 1.375],

        "nr2": [-6.83210861e-2, -3.47523515e-2, 1.04637008e-1, -1.09884198e-2,
                -0.125124331, -5.53450960e-3, -1.51182884e-2, -2.04800000e-2],
        "d2": [1, 1, 2, 5, 1, 1, 4, 2],
        "t2": [0, 2.375, 2., 2.125, 3.5, 6.5, 4.75, 12.5],
        "c2": [1, 1, 1, 1, 2, 2, 2, 3],
        "gamma2": [1]*8}

    eq = setzmann, MBWR, GERG, friend, shortSpan, sun

    _surface = {"sigma": [0.03825, -0.006024, -0.0007065],
                "exp": [1.191, 5.422, 0.6161]}
    _dielectric = {"eq": 3, "Tref": 273.16, "rhoref": 1000.,
                   "a0": [],  "expt0": [], "expd0": [],
                   "a1": [6.5443, 0.0133], "expt1": [0, 1], "expd1": [1, 1],
                   "a2": [8.4578, 3.7196, -352.97, -100.65],
                   "expt2": [0, 1, 0, 1], "expd2": [2, 2, 3, 3]}
    _melting = {"eq": 1, "Tref": Tt, "Pref": 11.696,
                "Tmin": Tt, "Tmax": 625.0,
                "a1": [1, 0.247568e5, -0.736602e4, -0.247568e5, 0.736602e4],
                "exp1": [0, 1.85, 2.1, 0, 0],
                "a2": [], "exp2": [], "a3": [], "exp3": []}
    _sublimation = {"eq": 3, "Tref": Tt, "Pref": 11.696,
                    "Tmin": Tt, "Tmax": Tt,
                    "a1": [], "exp1": [],
                    "a2": [-12.84], "exp2": [1],
                    "a3": [], "exp3": []}
    _vapor_Pressure = {
        "eq": 6,
        "ao": [-6.036219, 1.409353, -0.4945199, -1.443048],
        "exp": [2, 3, 4, 9]}
    _liquid_Density = {
        "eq": 3,
        "ao": [1.9906389, -0.78756197, 0.036976723],
        "exp": [0.354, 0.5, 2.5]}
    _vapor_Density = {
        "eq": 4,
        "ao": [-1.880284, -2.8526531, -3.000648, -5.251169, -13.191859, -37.553961],
        "exp": [1.062, 2.5, 4.5, 7.5, 12.5, 23.5]}

    visco0 = {"eq": 4, "omega": 1,
              "__name__": "Quiñones-Cisneros (2011)",
              "__doi__": {"autor": "S.E.Quinones-Cisneros, M.L. Huber and U.K. Deiters",
                  "title": "Reference Correlation for the Viscosity of Methane",
                  "ref": "High Temperatures - High Pressures 32(1) 73 – 81",
                  "doi": ""},

              "Tref": 190.564, "muref": 1.0,
              "ek": 174., "sigma": 0.36652, "n_chapman": 0,
              "n_ideal": [0.028790445329809258e3, -0.08883896490106571e3,
                          0.0854278871311819e3, -0.018038099301409677e3],
              "t_ideal": [0, 0.25, 0.5, 0.75],

              "a": [-3.388499774849180e-5, 1.357751056436950e-5, 0.0],
              "b": [2.757578135745610e-5, -3.437257168370160e-5, 0.0],
              "c": [2.891185964062900e-5, -9.980820268031560e-6, -2.073683069612580e-7],
              "A": [1.599928656708460e-8, -1.914111948640950e-9, 0.0],
              "B": [-2.591543952601510e-9, 3.260205780076830e-9, 0.0],
              "C": [-3.328762135404730e-8, 1.806469586530360e-7, 4.380464338668540e-10],
              "D": [3.151938769973220e-12, 0.0, 0.0]}

    visco1 = {"eq": 1, "omega": 1,
              "collision": [0.215309028, -0.46256942, 0.051313823,
                            0.030320660, -0.0070047029],
              "__name__": "Vogel (2000)",
              "__doi__": {"autor": "Vogel, E., Wilhelm, J., Kuechenmeister, C., and Jaesche, M.",
                  "title": "High-precision viscosity measurements on methane",
                  "ref": "High Temperatures - High Pressures 32(1) 73 – 81",
                  "doi": "10.1068/htwu359"},

              "ek": 160.78, "sigma": 0.37333,
              "n_chapman": 0.0855422/M**0.5,

              "n_virial": [-19.572881, 219.73999, -1015.3226, 2471.01251,
                           -3375.1717, 2491.6597, -787.26086, 14.085455,
                           -0.34664158],
              "t_virial": [0, -0.25, -0.5, -0.75, -1, -1.25, -1.5, -2.5, -5.5],
              "Tref_virial": 159.7, "etaref_virial": 0.0306525,

              "Tref_res": 190.564, "rhoref_res": 10.139*M, "etaref_res": 1,
              "n_packed": [3.10860501398],
              "t_packed": [0],
              "n_poly": [-3.02256904347, 17.6965130175, 3.11150846518,
                         -21.5685107769, 0.672852409238, 10.2387524315,
                         -1.09330775541, -1.20030749419, -21.1009923406],
              "t_poly": [0, -1, 0, -1, 0, -1, 0, -1, 0],
              "d_poly": [2, 2, 3, 3, 4, 4, 5, 5, 1],
              "g_poly": [0, 0, 0, 0, 0, 0, 0, 0, -1],
              "c_poly": [0, 0, 0, 0, 0, 0, 0, 0, 0],
              "n_num": [21.1009923406],
              "t_num": [0],
              "d_num": [1],
              "g_num": [0],
              "c_num": [0],
              "n_den": [1, -1],
              "t_den": [0, 0],
              "d_den": [0, 1],
              "g_den": [1, 0],
              "c_den": [0, 0]}

    visco2 = {"eq": 2, "omega": 2,
              "__name__": "Younglove (1987)",
              "__doi__": {"autor": "Younglove, B.A. and Ely, J.F.",
                          "title": "Thermophysical Properties of Fluids. II. Methane, Ethane, Propane, Isobutane, and Normal Butane ",
                          "ref": "J. Phys. Chem. Ref. Data 16, 577 (1987)",
                          "doi": "10.1063/1.555785"},

              "ek": 168., "sigma": 0.368,
              "n_chapman": 0.1069188/M**0.5,
              "F": [0.16969859271, -0.13337234608e-1, 0.140e1, 0.168e3],
              "E": [-0.1620427429e2, 0.4270589027e3, 0.1402596278e2,
                    -0.3916837745e4, -0.347709909e-1, 0.2136542674e2,
                    0.1436802482e4],
              "rhoc": 10.15}

    visco3 = {"eq": 1, "omega": 2,
              "__name__": "Friend (1989)",
              "__doi__": {"autor": "Friend, D.G., Ely, J.F., and Ingham, H.",
                          "title": "Thermophysical Properties of Methane",
                          "ref": "J. Phys. Chem. Ref. Data 18, 583 (1989)",
                          "doi": "10.1063/1.555828"},

              "Tref": 174., "etaref": 10.0,
              "ek": 174., "sigma": 0.36652,
              "n_chapman": 0.14105376/M**0.5,

              "Tref_res": 190.551, "rhoref_res": 10.139*M, "etaref_res": 12.149,
              "n_num": [0.41250137, -0.14390912, 0.10366993, 0.40287464,
                        -0.24903524, -0.12953131, 0.06575776, 0.02566628,
                        -0.03716526],
              "t_num": [0, -1, 0, -1, -1.5, 0, -2, 0, -1],
              "d_num": [1, 1, 2, 2, 2, 3, 3, 4, 4],
              "g_num": [0, 0, 0, 0, 0, 0, 0, 0, 0],
              "c_num": [0, 0, 0, 0, 0, 0, 0, 0, 0],
              "n_den": [1.0, -0.38798341, 0.03533815],
              "t_den": [0, 0, -1.0],
              "d_den": [0, 1, 1],
              "g_den": [0, 0, 0],
              "c_den": [0, 0, 0]}

    _viscosity = visco0, visco1, visco2, visco3

    thermo0 = {"eq": 1, "critical": "CH4",
               "__name__": "Friend (1989)",
               "__doi__": {"autor": "Friend, D.G., Ely, J.F., and Ingham, H.",
                           "title": "Thermophysical Properties of Methane",
                           "ref": "J. Phys. Chem. Ref. Data 18, 583 (1989)",
                           "doi": "10.1063/1.555828"},

               "Tref": 174., "kref": 1e-3,
               "no": [1.45885, -0.4377162, 0],
               "co": [0, -1, -96],

               "Trefb": 190.551, "rhorefb": 10.139, "krefb": 6.29638e-3,
               "nb": [1.5554612, 1., 2.4149207, 0.55166331, -0.52837734,
                      0.073809553, 0.24465507, -0.047613626],
               "tb": [0, 0, 0, 0, 0, -1, 0, -1],
               "db": [2, 0, 1, 3, 4, 4, 5, 5],
               "cb": [0, -99, 0, 0, 0, 0, 0, 0]}

    thermo1 = {"eq": 2, "omega": 2,
               "__name__": "Younglove (1987)",
               "__doi__": {"autor": "Younglove, B.A. and Ely, J.F.",
                           "title": "Thermophysical Properties of Fluids. II. Methane, Ethane, Propane, Isobutane, and Normal Butane ",
                           "ref": "J. Phys. Chem. Ref. Data 16, 577 (1987)",
                           "doi": "10.1063/1.555785"},

               "visco": visco2,
               "n_chapman": 0.1069188,
               "G": [0.1346953698e1, -0.3254677753],
               "E": [0.2325800819e-2, -0.2477927999, 0.3880593713e2,
                     -0.1579519146e-6, 0.3717991328e-2, -0.9616989434,
                     -0.3017352774e-1, 0.4298153386],

               "critical": 2,
               "X": [37.42368, 3.16714, 0.78035, 0.60103],
               "Z": 6.512707e-10}

    _thermal = thermo0, thermo1


class Test(TestCase):

    def test_setzmann(self):
        # Selected point from Table 39, Pag 1117, saturation state
        st = CH4(T=90.694, x=0.5)
        self.assertEqual(round(st.P.MPa, 6), 0.011696)
        self.assertEqual(round(st.Liquido.rho, 2), 451.48)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -982.76)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -7.3868)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 2.1677)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 3.3678)
        self.assertEqual(round(st.Liquido.w, 1), 1538.6)
        self.assertEqual(round(st.Gas.rho, 5), 0.25074)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -438.50)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -1.3857)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.5735)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 2.1100)
        self.assertEqual(round(st.Gas.w, 2), 249.13)

        st = CH4(T=100, x=0.5)
        self.assertEqual(round(st.P.MPa, 6), 0.034376)
        self.assertEqual(round(st.Liquido.rho, 2), 438.89)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -951.21)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -7.0562)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 2.1136)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 3.4084)
        self.assertEqual(round(st.Liquido.w, 1), 1452.0)
        self.assertEqual(round(st.Gas.rho, 5), 0.67457)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -420.73)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -1.7514)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.5887)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 2.1458)
        self.assertEqual(round(st.Gas.w, 2), 260.09)

        st = CH4(T=110, x=0.5)
        self.assertEqual(round(st.P.MPa, 6), 0.088130)
        self.assertEqual(round(st.Liquido.rho, 2), 424.78)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -916.75)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -6.7290)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 2.0642)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 3.4692)
        self.assertEqual(round(st.Liquido.w, 1), 1354.7)
        self.assertEqual(round(st.Gas.rho, 4), 1.5982)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -402.92)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -2.0578)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.6108)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 2.2053)
        self.assertEqual(round(st.Gas.w, 2), 270.01)

        st = CH4(T=120, x=0.5)
        self.assertEqual(round(st.P.MPa, 5), 0.19143)
        self.assertEqual(round(st.Liquido.rho, 2), 409.90)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -881.54)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -6.4248)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 2.0196)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 3.5493)
        self.assertEqual(round(st.Liquido.w, 1), 1253.5)
        self.assertEqual(round(st.Gas.rho, 4), 3.2619)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -386.93)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -2.3030)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.6390)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 2.2930)
        self.assertEqual(round(st.Gas.w, 2), 277.76)

        st = CH4(T=140, x=0.5)
        self.assertEqual(round(st.P.MPa, 5), 0.64118)
        self.assertEqual(round(st.Liquido.rho, 2), 376.87)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -807.74)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -5.8653)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 1.9452)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 3.8129)
        self.assertEqual(round(st.Liquido.w, 1), 1037.7)
        self.assertEqual(round(st.Gas.rho, 3), 10.152)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -362.60)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -2.6857)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.7172)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 2.6108)
        self.assertEqual(round(st.Gas.w, 2), 285.93)

        st = CH4(T=160, x=0.5)
        self.assertEqual(round(st.P.MPa, 4), 1.5921)
        self.assertEqual(round(st.Liquido.rho, 2), 336.31)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -726.14)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -5.3391)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 1.9037)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 4.4354)
        self.assertEqual(round(st.Liquido.w, 2), 795.43)
        self.assertEqual(round(st.Gas.rho, 3), 25.382)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -353.87)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -3.0124)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 1.8473)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 3.4189)
        self.assertEqual(round(st.Gas.w, 2), 283.01)

        st = CH4(T=180, x=0.5)
        self.assertEqual(round(st.P.MPa, 4), 3.2852)
        self.assertEqual(round(st.Liquido.rho, 2), 276.23)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -625.00)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -4.7778)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 1.9669)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 4), 7.2923)
        self.assertEqual(round(st.Liquido.w, 2), 497.01)
        self.assertEqual(round(st.Gas.rho, 3), 61.375)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -378.11)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -3.4062)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 2.1404)
        self.assertEqual(round(st.Gas.cp.kJkgK, 4), 7.5740)
        self.assertEqual(round(st.Gas.w, 2), 266.04)

        st = CH4(T=190, x=0.5)
        self.assertEqual(round(st.P.MPa, 4), 4.5186)
        self.assertEqual(round(st.Liquido.rho, 2), 200.78)
        self.assertEqual(round(st.Liquido.h.kJkg, 2), -532.67)
        self.assertEqual(round(st.Liquido.s.kJkgK, 4), -4.3082)
        self.assertEqual(round(st.Liquido.cv.kJkgK, 4), 2.6022)
        self.assertEqual(round(st.Liquido.cp.kJkgK, 3), 94.012)
        self.assertEqual(round(st.Liquido.w, 2), 250.31)
        self.assertEqual(round(st.Gas.rho, 2), 125.18)
        self.assertEqual(round(st.Gas.h.kJkg, 2), -451.91)
        self.assertEqual(round(st.Gas.s.kJkgK, 4), -3.8831)
        self.assertEqual(round(st.Gas.cv.kJkgK, 4), 2.8546)
        self.assertEqual(round(st.Gas.cp.kJkgK, 2), 140.81)
        self.assertEqual(round(st.Gas.w, 2), 238.55)

        # Selected points from Table 40, Pag 1119
        st = CH4(T=90.698, P=2.5e4)
        self.assertEqual(round(st.rho, 2), 451.48)
        self.assertEqual(round(st.u.kJkg, 2), -982.78)
        self.assertEqual(round(st.h.kJkg, 2), -982.73)
        self.assertEqual(round(st.s.kJkgK, 4), -7.3868)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.1677)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.3677)
        self.assertEqual(round(st.w, 1), 1538.7)

        st = CH4(T=115, P=1e5)
        self.assertEqual(round(st.rho, 4), 1.7341)
        self.assertEqual(round(st.u.kJkg, 2), -450.34)
        self.assertEqual(round(st.h.kJkg, 2), -392.68)
        self.assertEqual(round(st.s.kJkgK, 4), -2.0301)
        self.assertEqual(round(st.cv.kJkgK, 4), 1.6041)
        self.assertEqual(round(st.cp.kJkgK, 4), 2.1957)
        self.assertEqual(round(st.w, 2), 276.16)

        st = CH4(T=110, P=101325)
        self.assertEqual(round(st.rho, 2), 424.79)
        self.assertEqual(round(st.u.kJkg, 2), -916.97)
        self.assertEqual(round(st.h.kJkg, 2), -916.74)
        self.assertEqual(round(st.s.kJkgK, 4), -6.7291)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.0642)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.4691)
        self.assertEqual(round(st.w, 1), 1354.8)

        st = CH4(T=620, P=5e5)
        self.assertEqual(round(st.rho, 4), 1.5546)
        self.assertEqual(round(st.u.kJkg, 2), 564.67)
        self.assertEqual(round(st.h.kJkg, 2), 886.30)
        self.assertEqual(round(st.s.kJkgK, 4), 1.1384)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.8272)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.3497)
        self.assertEqual(round(st.w, 2), 617.61)

        st = CH4(T=150, P=1e6)
        self.assertEqual(round(st.rho, 3), 15.536)
        self.assertEqual(round(st.u.kJkg, 2), -418.03)
        self.assertEqual(round(st.h.kJkg, 2), -353.67)
        self.assertEqual(round(st.s.kJkgK, 4), -2.8198)
        self.assertEqual(round(st.cv.kJkgK, 4), 1.7556)
        self.assertEqual(round(st.cp.kJkgK, 4), 2.8402)
        self.assertEqual(round(st.w, 2), 287.76)

        st = CH4(T=200, P=5e6)
        self.assertEqual(round(st.rho, 3), 87.764)
        self.assertEqual(round(st.u.kJkg, 2), -423.51)
        self.assertEqual(round(st.h.kJkg, 2), -366.54)
        self.assertEqual(round(st.s.kJkgK, 4), -3.4670)
        self.assertEqual(round(st.cv.kJkgK, 4), 1.9965)
        self.assertEqual(round(st.cp.kJkgK, 4), 7.2726)
        self.assertEqual(round(st.w, 2), 291.29)

        st = CH4(T=100, P=1e7)
        self.assertEqual(round(st.rho, 2), 446.02)
        self.assertEqual(round(st.u.kJkg, 2), -957.84)
        self.assertEqual(round(st.h.kJkg, 2), -935.42)
        self.assertEqual(round(st.s.kJkgK, 4), -7.1235)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.1389)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.3437)
        self.assertEqual(round(st.w, 1), 1525.7)

        st = CH4(T=600, P=5e7)
        self.assertEqual(round(st.rho, 2), 134.47)
        self.assertEqual(round(st.u.kJkg, 2), 400.24)
        self.assertEqual(round(st.h.kJkg, 2), 772.07)
        self.assertEqual(round(st.s.kJkgK, 4), -1.5109)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.8062)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.5887)
        self.assertEqual(round(st.w, 2), 786.69)

        st = CH4(T=420, P=1e8)
        self.assertEqual(round(st.rho, 2), 277.63)
        self.assertEqual(round(st.u.kJkg, 2), -165.97)
        self.assertEqual(round(st.h.kJkg, 2), 194.23)
        self.assertEqual(round(st.s.kJkgK, 4), -3.1391)
        self.assertEqual(round(st.cv.kJkgK, 4), 2.2570)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.1894)
        self.assertEqual(round(st.w, 1), 1096.5)

        st = CH4(T=620, P=1e9)
        self.assertEqual(round(st.rho, 2), 503.16)
        self.assertEqual(round(st.u.kJkg, 2), 350.14)
        self.assertEqual(round(st.h.kJkg, 2), 2337.56)
        self.assertEqual(round(st.s.kJkgK, 4), -3.1888)
        self.assertEqual(round(st.cv.kJkgK, 4), 3.2951)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.8115)
        self.assertEqual(round(st.w, 1), 2915.6)

    def test_shortSpan(self):
        # Table III, Pag 46
        st = CH4(T=700, rho=200, eq="shortSpan")
        self.assertEqual(round(st.cp0.kJkgK, 4), 3.6278)
        self.assertEqual(round(st.P.MPa, 3), 108.108)
        self.assertEqual(round(st.cp.kJkgK, 4), 3.9282)

        st2 = CH4(T=750, rho=100, eq="shortSpan")
        self.assertEqual(round(st2.h.kJkg-st.h.kJkg, 2), 142.73)
        self.assertEqual(round(st2.s.kJkgK-st.s.kJkgK, 5), 0.78166)

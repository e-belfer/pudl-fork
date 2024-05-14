"""Add electric sector generation table from AEO

Revision ID: 53aababa3b9d
Revises: e0d3904b97f4
Create Date: 2024-04-27 09:31:11.802185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53aababa3b9d'
down_revision = '110e61b9108d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('core_eiaaeo__yearly_projected_generation_in_electric_sector_by_technology',
    sa.Column('report_year', sa.Integer(), nullable=False, comment='Four-digit year in which the data was reported.'),
    sa.Column('electricity_market_module_region_eiaaeo', sa.Enum('florida_reliability_coordinating_council', 'midcontinent_central', 'midcontinent_east', 'midcontinent_south', 'midcontinent_west', 'northeast_power_coordinating_council_new_england', 'northeast_power_coordinating_council_new_york_city_and_long_island', 'northeast_power_coordinating_council_upstate_new_york', 'pjm_commonwealth_edison', 'pjm_dominion', 'pjm_east', 'pjm_west', 'serc_reliability_corporation_central', 'serc_reliability_corporation_east', 'serc_reliability_corporation_southeastern', 'southwest_power_pool_central', 'southwest_power_pool_north', 'southwest_power_pool_south', 'texas_reliability_entity', 'united_states', 'western_electricity_coordinating_council_basin', 'western_electricity_coordinating_council_california_north', 'western_electricity_coordinating_council_california_south', 'western_electricity_coordinating_council_northwest_power_pool_area', 'western_electricity_coordinating_council_rockies', 'western_electricity_coordinating_council_southwest'), nullable=False, comment='AEO projection region.'),
    sa.Column('model_case_eiaaeo', sa.Enum('aeo2022', 'high_economic_growth', 'high_macro_and_high_zero_carbon_technology_cost', 'high_macro_and_low_zero_carbon_technology_cost', 'high_oil_and_gas_supply', 'high_oil_price', 'high_uptake_of_inflation_reduction_act', 'high_zero_carbon_technology_cost', 'low_economic_growth', 'low_macro_and_high_zero_carbon_technology_cost', 'low_macro_and_low_zero_carbon_technology_cost', 'low_oil_and_gas_supply', 'low_oil_price', 'low_uptake_of_inflation_reduction_act', 'low_zero_carbon_technology_cost', 'no_inflation_reduction_act', 'reference'), nullable=False, comment='Factors such as economic growth, future oil prices, the ultimate size of domestic energy resources, and technological change are often uncertain. To illustrate some of these uncertainties, EIA runs side cases to show how the model responds to changes in key input variables compared with the Reference case. See https://www.eia.gov/outlooks/aeo/assumptions/case_descriptions.php for more details.'),
    sa.Column('projection_year', sa.Integer(), nullable=False, comment='The year of the projected value.'),
    sa.Column('technology_description_eiaaeo', sa.Enum('coal', 'combined_cycle', 'combustion_turbine_diesel', 'distributed_generation', 'diurnal_storage', 'fuel_cells', 'nuclear', 'oil_and_natural_gas_steam', 'pumped_storage', 'renewable_sources'), nullable=False, comment='Generation technology reported for AEO.'),
    sa.Column('summer_capacity_mw', sa.Float(), nullable=True, comment='The net summer capacity.'),
    sa.Column('summer_capacity_planned_additions_mw', sa.Float(), nullable=True, comment='The total planned additions to net summer generating capacity.'),
    sa.Column('summer_capacity_unplanned_additions_mw', sa.Float(), nullable=True, comment='The total unplanned additions to net summer generating capacity.'),
    sa.Column('summer_capacity_retirements_mw', sa.Float(), nullable=True, comment='The total retirements from to net summer generating capacity.'),
    sa.Column('gross_generation_mwh', sa.Float(), nullable=True, comment='Gross electricity generation for the specified period in megawatt-hours (MWh).'),
    sa.PrimaryKeyConstraint('report_year', 'electricity_market_module_region_eiaaeo', 'model_case_eiaaeo', 'projection_year', 'technology_description_eiaaeo', name=op.f('pk_core_eiaaeo__yearly_projected_generation_in_electric_sector_by_technology'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('core_eiaaeo__yearly_projected_generation_in_electric_sector_by_technology')
    # ### end Alembic commands ###
